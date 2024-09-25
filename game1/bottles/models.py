from django.db import models
from userapp.models import Player



class BottleItem(models.Model):
    name = models.CharField(max_length=100, default="bottle")
    max_characters = models.IntegerField(default=1000)
    points = models.IntegerField(default=0)
    distance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Bottle(models.Model):
    bottle_type = models.ForeignKey(BottleItem, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=True, null=True)
    response = models.CharField(max_length=1000, blank=True, null=True)
    sender = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sender')
    reader = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='reader')
    read_count = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.bottle_type.name


