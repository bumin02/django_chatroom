# from django.urls import path
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/message/(?P<chat_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]