from channels.generic.websocket import AsyncWebsocketConsumer
from dotenv import load_dotenv
from typing import Dict
from openai import OpenAI
import os
# from whisperproject import make_trans

load_dotenv()

class WhisperConsumer(AsyncWebsocketConsumer):
    client = OpenAI(
        api_key= os.getenv("OPENAI_API_KEY")
    )

    async def connect(self):
        await self.accept()

    async def get_transcript(self,data):
        with open("audiofile.wav","wb") as af:
            af.write(b'\x1aE\xdf\xa3\x01\x00\x00\x00\x00\x00\x00\x1fB\x86\x81\x01B\xf7\x81\x01B\xf2\x81\x04B\xf3\x81\x08B\x82\x84webmB\x87\x81\x02B\x85\x81\x02\x18S\x80g\x01\xff\xff\xff\xff\xff\xff\xff\x11M\x9bt\x01\x00\x00\x00\x00\x00\x00\x00\x15I\xa9f\x01\x00\x00\x00\x00\x00\x00I*\xd7\xb1\x83\x0fB@D\x89\x88\x00\x00\x00\x00\x00\x00\x00\x00M\x80\x98QTmuxingAppLibWebM-0.0.1WA\x99QTwritingAppLibWebM-0.0.1\x16T\xaek\x01\x00\x00\x00\x00\x00\x00`\xae\x01\x00\x00\x00\x00\x00\x00W\xd7\x81\x02s\xc5\x84\xcb\xb4\n;\x83\x81\x02V\xaa\x84\x00c.\xa0V\xbb\x84\x04\xc4\xb4\x00\x86\x86A_OPUSc\xa2\x93OpusHead\x01\x028\x01\x80\xbb\x00\x00\x00\x00\x00%\x86\x88\x84OPUS\xe1\x01'+data)
            # print("lawdasur",af)
        try:
            with open("audiofile.wav","rb") as af:
                # print("bobsaur",af.read())
                # af.seek(0)
                trans = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file = af,
                    language="en",
                )
            # print(trans)
            if trans:
                # print("asfhei")
                await self.send(trans.text)
        except Exception:
            # print("chud gaya")
            await self.send("")
        

    async def receive(self, bytes_data):
        print("recieve : ",
            #   bytes_data,
              )
        await self.get_transcript(bytes_data)

    async def disconnect(self, close_code):
       await self.close()