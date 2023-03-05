import schedule
import asyncio
from datetime import datetime, timedelta, time
import time
from threading import Thread




async def tg(temp):
    print(f'TELEGRAM START {temp}')
    #return schedule.CancelJob


def job_tg(name):
    print('Hello World',name)
    asyncio.run(tg(name))
    return schedule.CancelJob

def main_schedule_img(tepm_date,time_, text, phon, username,img):

    if tepm_date==1:
        print('DAy_1')
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        #schedule.every().seconds.do(job_tg, name=temp_text)
        schedule.every().monday.at(time_).do(job_tg, name=temp_text)

        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
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
        schedule.every().tuesday.at(time_).do(job_tg, name=temp_text)

        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
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
        schedule.every().wednesday.at(time_).do(job_tg, name=temp_text)
        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==4:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().thursday.at(time_).do(job_tg, name=temp_text)
        #job_4 = schedule.every().seconds.do(job_tg, name=temp_text)
        #schedule.run_pending()
        #schedule.every().seconds.do(job_tg, name=temp_text)

        while True:
            schedule.run_pending()
            #print(job_4)
            print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==5:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().friday.at(time_).do(job_tg, name=temp_text)
        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==6:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().saturday.at(time_).do(job_tg, name=temp_text)
        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)
    if tepm_date==7:
        temp_text={'text_mess': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img
                 }
        schedule.every().sunday.at(time_).do(job_tg, name=temp_text)
        while True:
            schedule.run_pending()
            print(schedule.get_jobs())
            if len(schedule.get_jobs()) < 1:
                break
            time.sleep(1)



#main_schedule_img(4, "04:25",'text_1', 'phon', 'username','img')


#asyncio.run(main_schedule(1, 'text_1', 'phon', 'username','img'))

#schedule.every().thursday.at("01:48").do(greet, name=test_text_1)
#schedule.every().seconds.do(job, name=test_text_3)


#
#
# #
# threads = [
#
#     Thread(target=main_schedule_img, args=(4, "04:35",'text_33', 'phon', 'username','img')),
# Thread(target=main_schedule_img, args=(4, "04:34",'text_34', 'phon', 'username','img')),
# Thread(target=main_schedule_img, args=(4, "04:35",'text_35', 'phon', 'username','img')),
# Thread(target=main_schedule_img, args=(4, "04:38",'text_38', 'phon', 'username','img'))
#            ]
#
# # Func1 and Func2 run in separate threads
# for thread in threads:
#     thread.start()
#
# # Wait until both Func1 and Func2 have finished
# for thread in threads:
#     thread.join()



t1 = Thread(target=main_schedule_img, args=(4, "04:58:00",'text_41', 'phon', 'username','img'))
t2 = Thread(target=main_schedule_img, args=(4, "04:58:02",'text_39', 'phon', 'username','img'))
t3 = Thread(target=main_schedule_img, args=(4, "04:58:03",'text_38', 'phon', 'username','img'))
t4 = Thread(target=main_schedule_img, args=(4, "04:58:05",'text_40', 'phon', 'username','img'))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t3.join()
