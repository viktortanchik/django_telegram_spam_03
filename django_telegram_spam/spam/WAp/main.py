import asyncio
import time

from alright import WhatsApp

messenger = WhatsApp()
messenger.find_user('380934787277')
#time.sleep(3)
# messenger.send_message('Не обращай внимания это тестовое сообщения 5')
#input()

img = '/home/viktor/Downloads/7-jdFo7tNz7-transformed.jpeg'
time.sleep(3)

messenger.send_picture(img, 'mess_img')
#input()


# messages = ['Не обращай внимания это тестовое сообщения 1', 'Не обращай внимания это тестовое сообщения 2']
# for message in messages:
#         time.sleep(3)
#         messenger.send_message(message)
# input('qwer')
#input()