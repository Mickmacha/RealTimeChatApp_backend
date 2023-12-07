# chat_app/urls.py

from django.urls import path
from .views import ChatRoomList, MessageList, index, room

# app_name = 'chat_app'
urlpatterns = [
    path('chat-rooms/', ChatRoomList.as_view(), name='chat-room-list'),
    path('messages/', MessageList.as_view(), name='message-list'),
    path('', index, name='index'),
    path("<str:room_name>/", room, name="room"),
]
