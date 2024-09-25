
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from .models import Player
from django.http import JsonResponse



class CreateUserView(APIView):
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



def view_table(request):
    player_list = Player.objects.all().order_by('all_count')  
    result = []
    for person in player_list:
        player_dict ={
            "name": person.user.username,
            "count":person.all_count
        }
        result.append(player_dict)
    return JsonResponse(result, safe =False)
