from django.urls import path
from . import views

urlpatterns = [
    path('', views.message, name='message'),
    # path('<slug:slug>/', views.message, name='message'),

    # path("", views.index, name="index"),

    # path('', views.messages, name='messages'),
    # path('slug<slug:slug>/', views.message, name='message'),

]