from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name='messages.urls'),
    path('<slug:slug>/', views.message, name='chat'),
]