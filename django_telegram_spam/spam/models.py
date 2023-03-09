from django.db import models
from django import forms
import time
#from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model,get_user
from django.conf import settings  # new
from django.utils import timezone
import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


User = get_user_model()


class User_settings(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)# work !!!
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    balance = models.CharField(max_length=100,blank=True)
    wallet = models.CharField(max_length=100,blank=True)
    hex_address = models.CharField(max_length=100,blank=True)
    private_key = models.CharField(max_length=100,blank=True)
    public_key = models.CharField(max_length=100,blank=True)
    text = models.CharField(max_length=100,blank=True)
    user_names = models.CharField(max_length=100,blank=True)
    tariff = models.CharField(max_length=100,blank=True)
    numbers = models.CharField(max_length=20,blank=True)
    date = models.DateTimeField(default=timezone.now)



    #makemigrations
    def __str__(self):
        return self.user.username

class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)#,default=User)# related_name='user_names'
    days_1 = models.BooleanField()
    days_2 = models.BooleanField()
    days_3 = models.BooleanField()
    days_4 = models.BooleanField()
    days_5 = models.BooleanField()
    days_6 = models.BooleanField()
    days_7 = models.BooleanField()
    texts = models.TextField(blank=False)

    TYPE_SELECT_account = (
        ('0', 'Indonesia account 1'),
        ('1', 'Vietnam account'),
        ('2', 'Indonesia account 2'),
    )
    TYPE_SELECT_spam_progress = (
        ('0', 'spam disabled'),
        ('1', 'spam enabled '),
    )
    TYPE_SELECT_spam_repeat = (
        ('0', 'Execute once'),
        ('1', 'Repeat all the time'),
    )
    TYPE_SELECT_spam_temp = (
        ('8', 'today it was shipped'),
        ('0', 'didnt send it today'),
    )
    account = models.CharField(max_length=20, choices=TYPE_SELECT_account,blank=False,default=1)
    status_spam = models.CharField(max_length=20, choices=TYPE_SELECT_spam_progress,blank=True,default=1)
    status_spam_repeat = models.CharField(max_length=20, choices=TYPE_SELECT_spam_repeat,blank=False,default=0)
    #status_spam_temp = models.CharField(max_length=20, choices=TYPE_SELECT_spam_temp,blank=True,default=8)
    status_spam_temp =  models.CharField(max_length=11,blank=True,default='2000-00-00')

    contact = models.CharField(max_length=128,blank=True)
    file = models.ImageField(upload_to='images/',blank=True)
    #date_send = models.DateField(default=timezone.now)
    time_send_days_1 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    time_send_days_2 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    time_send_days_3 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    time_send_days_4 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    time_send_days_5 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    time_send_days_6 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    time_send_days_7 = models.TimeField(default=datetime.time(hour=9, minute=0, second=0),blank=True)
    #date = models.DateTimeField(blank=True,null=True,default=timezone.now)
    # date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.user.username


if __name__ == '__main__':
    Subscriber()