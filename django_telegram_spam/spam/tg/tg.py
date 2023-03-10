from telethon import sync, events
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

import json
from telethon.tl.functions.account import GetAuthorizationsRequest
from datetime import timedelta
import asyncio
###########################################
import schedule
import asyncio
from datetime import datetime, timedelta, time
from threading import Thread
import time


#############################################

# async def main():
#     async with Client("6283834705843", api_id, api_hash) as app:
#         await app.send_message("674868256", "Greetings from **Pyrogram**!")
#

#asyncio.run(main())

'''
def handle_uploaded_file(f):
    with open('/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
handle_uploaded_file(request.FILES['file'])



'''



async def telega_text(temp_data):
    api_id = 16526653
    api_hash = "918872691e0a8ea8335cce787546eb3d"

    phone = '447405665250'
    # phone = '447535092381'
    # phone = '447476782487'
    # phone = '447476746907'

    if temp_data['phon'] == '0':
        phone = '447405665250'

    if temp_data['phon'] == '1':
        phone = '447535092381'

    if temp_data['phon'] == '2':
        phone = '447476782487'

    if temp_data['phon'] == '3':
        phone = '447476746907'
    print(f'phon>>>{temp_data["phon"]}   phone>>{phone}')

    client = TelegramClient(phone, api_id=api_id, api_hash=api_hash)
    try:
        await client.connect()
        #await app.send_melsssage("674868256", str(text))
        print('SEND_TEXT')
        await client.send_message(temp_data["username"],str( temp_data["text_mess"]))
        await client.disconnect()
        #return schedule.CancelJob

    except KeyError as er:
        print("Error>> ", er)
        #return schedule.CancelJob

        # async with Client("6283834705843", api_id, api_hash) as app:
    #     await app.send_message("674868256", str(text))


async def telega_img(temp_data):
    print(f" TELEGRAM DATA >>>>>  {temp_data}")
    api_id = 16526653
    api_hash = "918872691e0a8ea8335cce787546eb3d"

    phone = '447405665250'
    # phone = '447535092381'
    # phone = '447476782487'
    # phone = '447476746907'

    if temp_data['phon'] == '0':
        phone = '447405665250'

    if temp_data['phon'] == '1':
        phone = '447535092381'

    if temp_data['phon'] == '2':
        phone = '447476782487'

    if temp_data['phon'] == '3':
        phone = '447476746907'
    try:
        client = TelegramClient(phone, api_id=api_id, api_hash=api_hash)
        print(f' Был выбран {phone}')
        await client.connect()

        #await app.send_melsssage("674868256", str(text))
        #await app.send_message(username, str(text))
        #await client.send_message(temp_data['username'],message= temp_data['text_mess'], file=temp_data['img_name'] )

        await client.send_message(temp_data['username'],message= temp_data['text_mess'], file=temp_data['img_name'] )

        await client.disconnect()
        #return schedule.CancelJob

    except KeyError as er:
        print("Error>> ", er)
        #return schedule.CancelJob

        # async with Client("6283834705843", api_id, api_hash) as app:
    #     await app.send_message("674868256", str(text))




def job_tg_img(name):
    asyncio.run(telega_img(name))
    #return schedule.CancelJob

def job_tg_text(name):
    asyncio.run(telega_text(name))
    #return schedule.CancelJob

def main_schedule_img(tepm_date,time_, text, phon, username,img):

    if tepm_date==1:
        print('DAy_1')
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        #schedule.every().seconds.do(job_tg, name=temp_text)
        schedule.every().monday.at(time_).do(job_tg_img, name=temp_text)

        while True:
            schedule.run_pending()
            print(f'Время до следующего выполнения >>>{schedule.idle_seconds()}')
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==2:
        print('DAy_2')
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        # schedule.every().seconds.do(job_tg, name=temp_text)
        schedule.every().tuesday.at(time_).do(job_tg_img, name=temp_text)

        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==3:
        print('DAy_3')
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().wednesday.at(time_).do(job_tg_img, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            print(f'Время до следующего выполнения >>>{schedule.idle_seconds()}')

            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==4:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().thursday.at(time_).do(job_tg_img, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==5:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().friday.at(time_).do(job_tg_img, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==6:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().saturday.at(time_).do(job_tg_img, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==7:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().sunday.at(time_).do(job_tg_img, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)



def main_schedule_text(tepm_date,time_, text, phon, username):
    temp_text = {'text_mess': text,
                 'phon': phon,
                 'username': username,
                 }
    if tepm_date==1:
        print('DAy_1')

        #schedule.every().seconds.do(job_tg, name=temp_text)
        schedule.every().monday.at(time_).do(job_tg_text, name=temp_text)

        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==2:
        print('DAy_2')
        # schedule.every().seconds.do(job_tg, name=temp_text)
        schedule.every().tuesday.at(time_).do(job_tg_text, name=temp_text)

        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==3:
        print('DAy_3')
        schedule.every().wednesday.at(time_).do(job_tg_text, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==4:
        schedule.every().thursday.at(time_).do(job_tg_text, name=temp_text)
        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==5:
        schedule.every().friday.at(time_).do(job_tg_text, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==6:
        schedule.every().saturday.at(time_).do(job_tg_text, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==7:
        schedule.every().sunday.at(time_).do(job_tg_text, name=temp_text)
        while True:
            schedule.run_pending()
            #print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)


temp_text = {'text_mess': 'text',
             'phon': 0,
             'username': '@viktortanchik',
             'img_name': "/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/media/images/Screenshot_from_2023-02-28_14-13-58_wX97U21.png"
             }
#asyncio.run(telega_img(temp_text))