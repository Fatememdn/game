from django.contrib import admin
from .models import Bottle, BottleItem
admin.site.register(Bottle)

@admin.register(BottleItem)
class BottleAdmin(admin.ModelAdmin):
    list_display = ('points', 'distance')