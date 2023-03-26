# Generated by Django 4.1.7 on 2023-03-26 21:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.CharField(blank=True, max_length=100)),
                ('wallet', models.CharField(blank=True, max_length=256)),
                ('hex_address', models.CharField(blank=True, max_length=256)),
                ('private_key', models.CharField(blank=True, max_length=256)),
                ('public_key', models.CharField(blank=True, max_length=256)),
                ('text', models.CharField(blank=True, max_length=100)),
                ('user_names', models.CharField(blank=True, max_length=100)),
                ('tariff', models.CharField(blank=True, max_length=100)),
                ('numbers', models.CharField(blank=True, max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber_WAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_1', models.BooleanField()),
                ('days_2', models.BooleanField()),
                ('days_3', models.BooleanField()),
                ('days_4', models.BooleanField()),
                ('days_5', models.BooleanField()),
                ('days_6', models.BooleanField()),
                ('days_7', models.BooleanField()),
                ('texts', models.TextField()),
                ('account', models.CharField(choices=[('0', 'Indonesia account 1'), ('1', 'Vietnam account'), ('2', 'Indonesia account 2')], default=1, max_length=20)),
                ('status_spam', models.CharField(blank=True, choices=[('0', 'spam disabled'), ('1', 'spam enabled ')], default=1, max_length=20)),
                ('status_spam_repeat', models.CharField(choices=[('0', 'Execute once'), ('1', 'Repeat all the time')], default=0, max_length=20)),
                ('status_spam_temp', models.CharField(blank=True, default='2000-00-00', max_length=11)),
                ('contact', models.CharField(blank=True, max_length=128)),
                ('file', models.ImageField(blank=True, upload_to='images/')),
                ('time_send_days_1', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_2', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_3', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_4', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_5', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_6', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_7', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_1', models.BooleanField()),
                ('days_2', models.BooleanField()),
                ('days_3', models.BooleanField()),
                ('days_4', models.BooleanField()),
                ('days_5', models.BooleanField()),
                ('days_6', models.BooleanField()),
                ('days_7', models.BooleanField()),
                ('texts', models.TextField()),
                ('account', models.CharField(choices=[('0', 'Indonesia account 1'), ('1', 'Vietnam account'), ('2', 'Indonesia account 2')], default=1, max_length=20)),
                ('status_spam', models.CharField(blank=True, choices=[('0', 'spam disabled'), ('1', 'spam enabled ')], default=1, max_length=20)),
                ('status_spam_repeat', models.CharField(choices=[('0', 'Execute once'), ('1', 'Repeat all the time')], default=0, max_length=20)),
                ('status_spam_temp', models.CharField(blank=True, default='2000-00-00', max_length=11)),
                ('contact', models.CharField(blank=True, max_length=128)),
                ('file', models.ImageField(blank=True, upload_to='images/')),
                ('time_send_days_1', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_2', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_3', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_4', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_5', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_6', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('time_send_days_7', models.TimeField(blank=True, default=datetime.time(9, 0))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
