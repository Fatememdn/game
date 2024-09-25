from django.urls import path
from . import views
urlpatterns = [
    path('bottles/', views.BottleItemView.as_view()),
    path('send/', views.SendBottleView.as_view()),
    path('read/', views.Readtext.as_view()),
    path('active-response/', views.AddResponse.as_view()),
    path("send-response/", views.SendResponse.as_view()),


]