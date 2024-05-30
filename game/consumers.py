import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import signals
from django.dispatch import receiver
import channels.layers
from .models import ZodiacGameStatus, Role
from .serializers import ZodiacgameStatusSerializer
import threading
import time

def serialized(db):
    return {
        "turns": db.turns ,
        "challenge": db.challenge ,
        "challenger": db.challenger ,
        "challenger_wanters": db.challenger_wanters,
        "room_name": db.room_name ,
        "day": db.day  ,
        "speak_turn": db.speak_turn ,
        "magicman": db.magicman ,
        "bomber": db.bomber,
        "zodiac": db.zodiac ,
        "ocean": db.ocean ,
        "gunner_fake": db.gunner_fake ,
        "gunner_real": db.gunner_real ,
        "died": db.died ,
    }

@staticmethod
@receiver(signals.post_save, sender=ZodiacGameStatus)
async def order_offer_observer(sender, instance, **kwargs):
    room_name = '1'
    room_group_name = f"chat_{room_name}"
    layer = channels.layers.get_channel_layer()
    await layer.group_send(
            room_group_name, {"type": "chat.message", "turn": serialized(instance)}
    )


def asign_challenger(challenger):
    g = ZodiacGameStatus.objects.get()
    g.challenger = challenger
    g.save()


def turn_changer():
    
    for i in range(12):
        g = ZodiacGameStatus.objects.get()
        g.speak_turn = i+ 1
        g.save()
        time.sleep(1)
        g = ZodiacGameStatus.objects.get()
        if g.challenger != None :
            g.speak_turn = g.challenger
            g.challenger = None
            g.save()
            time.sleep(2)
        if i == 11 :
            g.speak_turn = 0
            g.save()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = '1'
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'challenger' in text_data_json:
            x = threading.Thread(target=asign_challenger, args=(text_data_json["challenger"],))
            x.start()

        if 'start' in text_data_json:
            x = threading.Thread(target=turn_changer)
            x.start()


    # Receive message from room group
    async def chat_message(self, event):
        message = event

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"result": message}))

