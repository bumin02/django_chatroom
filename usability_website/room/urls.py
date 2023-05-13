from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms.urls'),
    path('<slug:slug>/', views.room, name='room'), 
]