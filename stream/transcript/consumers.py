from channels.generic.websocket import AsyncWebsocketConsumer
from dotenv import load_dotenv
import asyncio
from typing import Dict
import whisper
from openai import OpenAI
import os

load_dotenv()

class WhisperConsumer(AsyncWebsocketConsumer):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    async def connect(self):
        await self.accept()

    async def get_transcript(self, data):
        if "channel" in data:
            transcript = self.client.audio.transcriptions.create(
                model= "whisper-1",
                file = data
            )
            if transcript:
                await self.send(transcript)

    async def receive(self, bytes_data):
        await self.get_transcript(bytes_data)

    async def disconnect(self, close_code):
       await self.channel_layer.group_discard(
           self.room_group_name,
           self.channel_name
       )