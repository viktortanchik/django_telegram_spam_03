#from .forms import SubscriberForm#,ExampleForm
from .models import Subscriber
from .tg.tg import main_schedule_img,main_schedule_text
import asyncio
from threading import Thread
from multiprocessing import Process

from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
##################################################
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.views import LogoutView,auth_logout
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib import messages

#########################
from .create_wallet import create_wallet

#sudo fuser -k 8000/tcp

##################################################

# Create your views here.
# def hotel_image_view(request):
#     form = HotelForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         if form.is_valid():
#             #pass
#             form.save()
#             #return redirect('success')
#     else:
#         #pass
#         form = HotelForm()
#     #return render(request, 'spam/hotel_image_form.html', {'form': form})
#     return render(request,'spam/hotel_image_form.html', locals())

# def user_s(request):
#     return request.user.username
def my_view(request):
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')


def get_wallet(request,id):
    news_show = User_settings.objects.get(pk=id)
    form = SubscriberForm_test( instance=news_show)
    if request.user.is_authenticated:
        form = SubscriberForm_test(request.POST, request.FILES or None, instance=news_show)
        print(f'form--->{news_show.wallet}')
        wallet = str(news_show.wallet)

        if request.method == "POST":
            if len(wallet) < 1 or wallet == None:
                print('Create Wallet')
                base58check_address,private_key,hex_address,public_key = create_wallet()
                post = form.save(commit=False)
                post.user = request.user
                post.wallet = base58check_address
                post.private_key = private_key
                post.hex_address = hex_address
                post.public_key = public_key
                post.save(update_fields=['wallet','private_key','hex_address','public_key'])
                return redirect('/')

            else:
                print('error create wallet')


            # post = form.save(commit=False)
            # post.user = request.user
            # post.save(update_fields=['text'])
            # return redirect('/')
    return render(request, 'account/get_wallet.html',
                      {'form':form,
                      'news_show':news_show,}
                      )


def user_settings(request,id):
    news_show = User_settings.objects.get(pk=id)
    form = SubscriberForm_test( instance=news_show)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SubscriberForm_test(request.POST, request.FILES or None, instance=news_show)
            post = form.save(commit=False)
            post.user = request.user
            post.save(update_fields=['text'])
            return redirect('/')
    return render(request, 'account/user_settings.html',
                      {'form':form,
                      'news_show':news_show,}
                      )


def spam_list(request,id):
    news_show = Subscriber.objects.get(pk=id)
    form = SubscriberForm(instance=news_show)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SubscriberForm(request.POST, request.FILES or None, instance=news_show)
            post = form.save(commit=False)
            post.user = request.user
            post.save(update_fields=['text'])
            return redirect('/')

    return render(request, 'spam/spam_pro.html',
                      {'form':form,
                      'news_show':news_show,}
                      )


def handle_uploaded_file(f):
    #with open('/home/viktortanchik/tg_dj_spam/django_telegram_spam_02/django_telegram_spam/media/'+f.name, 'wb+') as destination:
    with open('/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/media/'+f.name, 'wb+') as destination:
        file_name=''
        for chunk in f.chunks():
            destination.write(chunk)
            file_name=chunk
        return file_name


def send_mess(post,data):
    if len(str(post.file)) > 0:
        #img = '/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/media/' + str(post.file)
        img = '/home/viktortanchik/django_telegram_spam_03/django_telegram_spam/media/' + str(post.file)

        if (data.get('days_1') != None):
            Process(target=main_schedule_img, args=(1, data['time_send_days_1'], data['texts'], data['account'], data['contact'], img,)).start()

            # t1 = Thread(target=main_schedule_img, args=(1, data['time_send_days_1'], data['texts'], data['account'], data['contact'], img,))
            # t1.start()
        if (data.get('days_2') != None):
            Process(target=main_schedule_img, args=(2, data['time_send_days_2'], data['texts'], data['account'], data['contact'], img,)).start()

            # t1 = Thread(target=main_schedule_img, args=(2, data['time_send_days_2'], data['texts'], data['gender'], data['contact'], img,))
            # t1.start()
        if (data.get('days_3') != None):
            Process(target=main_schedule_img, args=(3, data['time_send_days_3'], data['texts'], data['account'], data['contact'], img,)).start()
            # t1 = Thread(target=main_schedule_img, args=(3, data['time_send_days_3'], data['texts'], data['gender'], data['contact'], img,))
            # t1.start()
        if (data.get('days_4') != None):
            #t1 = Thread(target=main_schedule_img, args=(4, data['time_send_days_4'], data['texts'], data['gender'], data['contact'], img,))
            Process(target=main_schedule_img, args=(4, data['time_send_days_4'], data['texts'], data['account'], data['contact'], img,)).start()
            # t1 = Process(target=main_schedule_img, args=(4, data['time_send_days_4'], data['texts'], data['gender'], data['contact'], img,))
            # t1.start()
            #t1.join()
        if (data.get('days_5') != None):
            t1 = Thread(target=main_schedule_img, args=(5, data['time_send_days_5'], data['texts'], data['account'], data['contact'], img,))
            t1.start()
        if (data.get('days_6') != None):
            t1 = Thread(target=main_schedule_img, args=(6, data['time_send_days_6'], data['texts'], data['account'], data['contact'], img,))
            t1.start()
        if (data.get('days_7') != None):
            t1 = Thread(target=main_schedule_img, args=(7, data['time_send_days_7'], data['texts'], data['account'], data['contact'], img,))
            t1.start()

        # img = '/home/viktortanchik/tg_dj_spam/django_telegram_spam_02/django_telegram_spam/media/'+str(post.file)
        # asyncio.run(telega_img(data["texts"], data["gender"], data["contact"],img ))
        # tepm_date=data["date_send"]+" "+data["time_send"]
        # text=data["texts"]
        # phon=data["gender"]
        # username=data["contact"]

        # t1 = Thread(target=start_Scheduler_img, args=(tepm_date, text, phon, username,img,))
        # t1.start()
        print('send OK img')
    else:

        if (data.get('days_1') != None):
            Process(target=main_schedule_text, args=(1, data['time_send_days_1'], data['texts'], data['account'], data['contact'], )).start()

            # t1 = Thread(target=main_schedule_text, args=(1, data['time_send_days_1'], data['texts'], data['gender'], data['contact'], ))
            # t1.start()
        if (data.get('days_2') != None):
            Process(target=main_schedule_text, args=(2, data['time_send_days_2'], data['texts'], data['account'], data['contact'], )).start()
            # t1 = Thread(target=main_schedule_text, args=(2, data['time_send_days_2'], data['texts'], data['gender'], data['contact'], ))
            # t1.start()
        if (data.get('days_3') != None):
            Process(target=main_schedule_text,
                    args=(3, data['time_send_days_3'], data['texts'], data['account'], data['contact'],)).start()
            # t1 = Thread(target=main_schedule_text, args=(3, data['time_send_days_3'], data['texts'], data['gender'], data['contact'], ))
            # t1.start()
        if (data.get('days_4') != None):
            #t1 = Thread(target=main_schedule_img, args=(4, data['time_send_days_4'], data['texts'], data['gender'], data['contact'], img,))
            Process(target=main_schedule_text, args=(4, data['time_send_days_4'], data['texts'], data['account'], data['contact'], )).start()
            # t1 = Process(target=main_schedule_img, args=(4, data['time_send_days_4'], data['texts'], data['gender'], data['contact'], img,))
            # t1.start()
            #t1.join()
        if (data.get('days_5') != None):
            Process(target=main_schedule_text,
                    args=(5, data['time_send_days_5'], data['texts'], data['account'], data['contact'],)).start()
            # t1 = Thread(target=main_schedule_text, args=(5, data['time_send_days_5'], data['texts'], data['gender'], data['contact'], ))
            # t1.start()
        if (data.get('days_6') != None):
            Process(target=main_schedule_text,
                    args=(6, data['time_send_days_6'], data['texts'], data['account'], data['contact'],)).start()
            # t1 = Thread(target=main_schedule_text, args=(6, data['time_send_days_6'], data['texts'], data['gender'], data['contact'], ))
            # t1.start()
        if (data.get('days_7') != None):
            Process(target=main_schedule_text,
                    args=(7, data['time_send_days_7'], data['texts'], data['account'], data['contact'],)).start()
            # t1 = Thread(target=main_schedule_text, args=(7, data['time_send_days_7'], data['texts'], data['gender'], data['contact'], ))
            # t1.start()
        print('send mess')


def spam_pro(request):
    form = SubscriberForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        if request.method == "POST":
            filename = request.FILES
            data = request.POST
            post = form.save(commit=False)

            if (data.get('days_1') != None) or( data.get('days_2') != None) or (data.get('days_3') != None) or (data.get('days_4') != None) or (data.get('days_5') != None) or (data.get('days_6') != None)or (data.get('days_7') != None):
                print(f'data OK ===>{data}')#<><><><> {data["time_send"]} {data["days_1"]} {data["days_2"]} {data["days_3"]}')
                #print(f'data===>{data["date_send"]}<><><><> {data["time_send"]} {data["days_1"]} {data["days_2"]} {data["days_3"]}')
                post.user = request.user
                post.save()
                print(f'POST ++++ >> {post.id}')
                print(f'POST ++++ >> {post.texts}')
                try:
                    # print(f'====>>{str(post.file)}')
                    # print(f'=len=>>{len(str(post.file))}')
                    #send_mess(post,data)
                    print('Data save')

                except:
                    # asyncio.run(telega_text(data["texts"], data["gender"], data["contact"]))
                    print(' ERROR  send mess')
            else:
                print('ERROR you dont ChOOse buttons ')
                #messages.success(request, 'не один из элементов не был выбран ')
                #return render(request, 'spam/spam_pro.html', locals())
                mes= 'This is an error message.'
                return render(request, 'spam/spam_pro.html', {'mes': mes,'form':form})



        return render(request, 'spam/spam_pro.html', locals())
        # return render(request, 'base.html', {'form': form})
    else:
        # form = LoginForm(request.POST)
        # form = LoginForm()

        #print('login>>>')
        # return render(user_login,  locals())
        return redirect('/login')
        # return HttpResponse('Invalid login')


def index(request):

    form = SubscriberForm(request.POST, request.FILES)

    if request.user.is_authenticated:
        print(f'request.user.id---->>>{request.user.id}')
        if request.method == "POST":
            pass
        return render(request,'spam/home.html', locals())
        #return render(request, 'base.html', {'form': form})
    else:

        return redirect('/login')
        #return HttpResponse('Invalid login')

    #form = SubscriberForm(request.POST)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated successfully')
                    #return render(request, 'spam/index.html', {'form': form})
                    #return render(request, 'base.html', {'form': form})
                    return redirect('/')
                    #return render(request, 'login.html', {'form': form})

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/')
    #return render(request,'base.html', locals())


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        #form = SubscriberForm_test() # ТО что я хочу что бы создалосб в момент регистрации
        if user_form.is_valid():
            print(f"user_form>>>>>>>>{user_form}")
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # form.is_valid()
            # form.save() # В момент сохранения выбивает ошибку


            #return render(request, 'account/register_done.html', {'new_user': new_user})
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

