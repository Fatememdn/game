from django.shortcuts import render
from .models import BottleItem, Bottle
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .serializers import ShowBottleSerializer, SendBottleSerializer, Read, SendResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError 
from userapp.models import Player
import random 
from rest_framework.response import Response
from datetime import date  

# add bottle(-) , get bottle, read bottle(+) if user point == xx : can response  , limit reading

class BottleItemView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BottleItem.objects.all()
    serializer_class = ShowBottleSerializer

class SendBottleView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bottle.objects.all()
    serializer_class = SendBottleSerializer
    def perform_create(self, serializer):
        try:
            bottle_name  = self.request.data.get("bottle_name")
            bottle_item = BottleItem.objects.filter(name = bottle_name).first()
            if not bottle_item:
                raise ValidationError("Bottle item not found.")
            bootle_points = bottle_item.points
            sender = self.request.user.player
            text = self.request.data.get('text')

            if bootle_points > sender.points:
                raise ValidationError("You don't have enough points.")
            elif bottle_item.max_characters < len(text):
                raise ValidationError("Your message is too long for this bottle.")

            sender.points -= bootle_points
            sender.save()

            players = Player.objects.all()
            result = [
                person for person in players
                if ((-person.x + sender.x) ** 2 + (sender.y - person.y) ** 2) > 0
                and (((-person.x + sender.x) ** 2 + (sender.y - person.y) ** 2) ** 0.5) < bottle_item.distance
            ]

            if not result:
                raise ValidationError("No players available within distance.")

            random_num = random.randint(0, len(result) - 1)
            reader = result[random_num]

            bottle = Bottle.objects.create(bottle_type=bottle_item, sender=sender, text=text, reader=reader)
            return bottle

        except Exception as e:
                raise ValidationError(f"error: {str(e)}")


class Readtext(ListAPIView):  
    permission_classes = [IsAuthenticated]
    serializer_class = Read  

    def get_queryset(self):  
        bottle_list = Bottle.objects.filter(reader=self.request.user)  
        player = self.request.user  

        if player.last_text_read != date.today():  
            player.bottle_count = 0  
            player.last_text_read = date.today()  
            player.save()  

        if player.bottle_count < 3:  
            current_request = None  
            for obj in bottle_list:  
                if obj.read_count == 0:  
                    obj.read_count = 1  
                    obj.save()  
                    current_request = obj  
                    player.bottle_count += 1  
                    player.all_count += 1 
                    player.points += 100
                    player.save()  
                    break  
            
            if current_request is not None:  
                return [current_request]  
            else:  
                raise ValidationError("No unread bottles available.")  

        else:  
            return Response({"message": "You can't read more messages today."}, status=403) 
        

class AddResponse(UpdateAPIView):  
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):  
        player = self.request.user  
        if player.points >= 1000:  
            player.points -= 1000  
            player.response = True
            player.save()  
            serializer.save()
            return Response({"message": "Response added successfully."})  
        else:  
            raise ValidationError("Insufficient points to add response.") 
        

class SendResponse(UpdateAPIView):  
    queryset = Bottle.objects.all()  
    serializer_class = SendResponse 
    permission_classes = [IsAuthenticated] 

    def update(self, request, *args, **kwargs):  
        instance = self.get_object()  
        player = request.user  
       
        if instance.reader != player:  
            raise ValidationError("You are not allowed to respond to this bottle.")  
        elif instance.response is not None:  
            raise ValidationError("This bottle already has a response.")  
        elif getattr(player, 'response', True) == False:  
            raise ValidationError("You are not allowed to respond.")  
 
        response_text = self.request.data.get("text")  
        instance.response = response_text  
        instance.save()  
        return Response({"response": response_text})
            

