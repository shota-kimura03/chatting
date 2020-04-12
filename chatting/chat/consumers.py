from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import DatabaseSyncToAsync
import json
from .models import ChatLog
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # 元のコードは→self.room_group_name = 'chat_%s' % self.room_name
        self.room_group_name = 'chat_{}'.format(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send Data Insert to Database.
        userName = text_data_json['userName']
        sendId = text_data_json['sendId']
        recvId = text_data_json['recvId']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'userName': userName,
                'sendId': sendId,
                'recvId': recvId
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        userName = event['userName']
        sendId = event['sendId']
        recvId = event['recvId']
        await self._save_message(sendId=sendId, recvId=recvId, message=message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'userName': userName,
            'sendId': sendId,
            'recvId': recvId
        }))


    @DatabaseSyncToAsync
    def _save_message(self, sendId, recvId, message):
        ChatLog.objects.create(
            sendId=sendId,
            recvId=recvId,
            message=message,
            sendTime=timezone.now()
        )
