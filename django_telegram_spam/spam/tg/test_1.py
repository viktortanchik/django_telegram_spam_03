import os
from telethon import sync, events
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

import json
from telethon.tl.functions.account import GetAuthorizationsRequest
from datetime import timedelta

api_id = 20679883
api_hash = "9b2dc7f8eb7075861e9618448c3a78e4"

#phone = '447405665250'
#phone = '447535092381'
#phone = '447476782487'
phone = '447476746907'



app = TelegramClient(phone, api_id=api_id, api_hash=api_hash)

app.connect()
text='test'
app.send_message('@viktortanchik', str(text))