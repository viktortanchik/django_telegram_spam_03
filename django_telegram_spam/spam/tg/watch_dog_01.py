import asyncio
import sqlite3
import datetime
from multiprocessing import Process


# Подключаемся к базе данных
def get_task():
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/db.sqlite3')
    # Создаем объект-курсор для выполнения запросов
    cursor = conn.cursor()
    # Получаем содержимое таблицы spam_subscriber
    cursor.execute('SELECT * FROM spam_subscriber')
    columns = [col[0] for col in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return result

#print(get_task())
#изменения значения в базе

def update_status_spam(subscriber_id, status):
    conn = sqlite3.connect('/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE spam_subscriber SET status_spam = '{status}' WHERE id = {subscriber_id}")
    conn.commit()
    conn.close()




def update_status_spam_temp(id, new_status):
    # открываем соединение с базой данных
    conn = sqlite3.connect('/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/db.sqlite3')
    c = conn.cursor()

    # обновляем значение столбца для заданного ряда
    c.execute("UPDATE spam_subscriber SET status_spam_temp = ? WHERE id = ?", (new_status, id))

    # сохраняем изменения
    conn.commit()

    # закрываем соединение с базой данных
    conn.close()
def main():
    # создаем объект datetime для текущей даты
    today = datetime.datetime.today()
    # получаем номер дня недели (понедельник - 0, воскресенье - 6)
    day_of_week = today.weekday()
    if int(day_of_week) ==0:
        day_of_week=1
    else:
        day_of_week=day_of_week+1
    print("Номер дня недели:", day_of_week)

    tasks = get_task()
    #print(get_task())
    #Process(target=main_schedule_img, args=(1, data['time_send_days_1'], data['texts'], data['account'], data['contact'], img,)).start()
    for task in tasks:
        current_date = datetime.datetime.now().date()
        now = datetime.datetime.now()
        #print(task['time_send_days_3'][:5]  ,'  ',  now.strftime("%H:%M"))
        print(f"file >> {task}")

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_1']==1) and (task['time_send_days_1'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
                img = '/home/viktortanchik/django_telegram_spam_03/django_telegram_spam/media/' + str(task['file'])
                Process(target=main_schedule_img, args=(
                1, task['time_send_days_1'], task['texts'], task['account'], task['contact'], img,)).start()

            else:
                print('ОТПРАВКА ON IMG ')
                Process(target=main_schedule_text,
                        args=(1, task['time_send_days_1'], task['texts'], task['account'], task['contact'],)).start()

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_2']==1) and (task['time_send_days_2'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
            else:
                print('ОТПРАВКА ON IMG ')

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_3']==1) and (task['time_send_days_3'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
            else:
                print('ОТПРАВКА ON IMG ')

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_4']==1) and (task['time_send_days_4'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
            else:
                print('ОТПРАВКА ON IMG ')

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_5']==1) and (task['time_send_days_5'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
            else:
                print('ОТПРАВКА ON IMG ')

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_6']==1) and (task['time_send_days_6'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
            else:
                print('ОТПРАВКА ON IMG ')

        #    проверяем день недели                   проверяем время                   проверяем нужно ли выполнять     проверяем выполняли сегодня
        if (task['days_7']==1) and (task['time_send_days_7'][:5]==now.strftime("%H:%M"))and int(task['status_spam'])==1 and str(task['status_spam_temp'])!=str(current_date):
            # если нужно отправить только один раз
            if int(task['status_spam_repeat'])==0:
                update_status_spam(task['id'], 0)
                print(f'spam disabled>>{task["id"]} ')
            # изменяем для указания что мы сегодня уже отправляли это сообщения
            update_status_spam_temp(task['id'], str(current_date))
            if len(task['file']) > 0:
                print('ОТПРАВКА ')
                print('ОТПРАВКА c изображением')
            else:
                print('ОТПРАВКА ON IMG ')


            #pass
    #     # print(now.strftime("%H:%M"))
    #     # print(task[21])
    #     # print(task[day_of_week+12][:5])
    #     #    проверяеть день недели                   проверяет время                   проверяет нужно ли выполнять (после меняет значение если это не еженедельный запуск)
    #     if (task[day_of_week]==1)and (task[day_of_week+12][:5]==now.strftime("%H:%M")) and int(task[21])==1:
    #         print('ОТПРАВКА ')
    #         if int(task[10])==1:
    #             pass
    #         else:
    #             pass


#    query = f"UPDATE 'spam_subscriber' SET status_spam = ? {conditions}"

main()