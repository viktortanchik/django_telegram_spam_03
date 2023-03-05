import datetime as dt
#/usr/local/lib/python3.7/dist-packages/django/conf/project_template/
from scheduler import Scheduler
import asyncio

#from scheduler.asyncio import Scheduler

from scheduler.trigger import Monday, Tuesday
import time
from threading import Thread





async def main_2(text_test,phon,username):
    print('START!!!!!!!')
    print("WORK!!!")
    print(text_test,phon,username)


def foo(text_test,phon,username):
    asyncio.run(main_2(text_test,phon,username))
    print(f'test#########################################')
    # while True:
    #     print('WORK')
    #     time.sleep(2)
    #schedule.delete_jobs()
    #schedule.delete_job(j1)

    #
    # date_time_obj = dt.datetime.strptime(tepm_data, '%Y-%m-%d %H:%M')
    # print(date_time_obj)




async def task(tepm_date,text,phon,username):
    schedule = Scheduler()
    # loop = asyncio.get_running_loop()
    # schedule = Scheduler(loop=loop)

    flag = True
    temp_data = {'text_test': text,
                 'phon': phon,
                 'username': username
                 }
    #j1 =schedule.once(dt.datetime.strptime(tepm_date, '%Y-%m-%d %H:%M'), foo, kwargs = temp_data)
    j1 =schedule.once(Monday(), foo, kwargs = temp_data)
    j2 =schedule.once(Tuesday(), foo, kwargs = temp_data)
    j3 =schedule.once(Monday(), foo, kwargs = temp_data)
    j4 =schedule.once(Tuesday(), foo, kwargs = temp_data)
    j5 =schedule.once(Monday(), foo, kwargs = temp_data)
    #asyncio.run(main())

    while flag:
        schedule.exec_jobs()
        print(schedule)
        print(f'j1>>>{j1.attempts}')
        if j1.attempts ==1:
            flag=False
        time.sleep(10)

    print('END')

tepm_date='2023-01-11 07:51'
text ='sum_text'
phon='123456789'
username='@123asdfsd'

def main(tepm_date,text,phon,username):
    asyncio.run(task(tepm_date,text,phon,username))

t1 = Thread(target=main,args=(tepm_date,text,phon,username,))
t1.start()
while True:
    print('###### WORKS #####')
    time.sleep(2)

#