from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=500)
    x = models.IntegerField()
    y = models.IntegerField()
    bottle_count = models.PositiveIntegerField(default=0)
    all_count = models.PositiveIntegerField(default=0)
    last_text_read = models.DateField()
    response = models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return self.user.username





