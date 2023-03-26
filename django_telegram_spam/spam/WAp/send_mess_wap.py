import time

from alright import WhatsApp

#input()
#messenger.login()


def job_wpa_text(temp_data):
    messenger = WhatsApp()
    time.sleep(3)
    messenger.find_user(str(temp_data['number']))#'380934787277'
    time.sleep(3)
    messenger.send_message(temp_data['text_mess'])
    time.sleep(5)

    # messages = ['Не обращай внимания это тестовое сообщения 1', 'Не обращай внимания это тестовое сообщения 2']
    # for message in messages:
    #         messenger.send_message(message)
    # input('qwer')

def job_wpa_img(temp_data):
    messenger = WhatsApp()
    time.sleep(3)
    messenger.find_user(str(temp_data['number']))#'380934787277'
    time.sleep(3)
    messenger.send_picture(temp_data['img_name'],temp_data['text_mess'])
    time.sleep(5)

    # messages = ['Не обращай внимания это тестовое сообщения 1', 'Не обращай внимания это тестовое сообщения 2']
    # for message in messages:
    #         messenger.send_message(message)
    # input('qwer')