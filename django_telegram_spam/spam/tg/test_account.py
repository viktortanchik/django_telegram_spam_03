import time
from pyrogram import Client, filters
import asyncio
###########################################
import datetime as dt

from scheduler import Scheduler
#from scheduler.asyncio import Scheduler

from scheduler.trigger import Monday, Tuesday
import time
from threading import Thread


#############################################
api_id = 20679883
api_hash = "9b2dc7f8eb7075861e9618448c3a78e4"

async def main():
    async with Client("6283834705843", api_id, api_hash) as app:
        await app.send_message("674868256", "Greetings from **Pyrogram**!")


asyncio.run(main())