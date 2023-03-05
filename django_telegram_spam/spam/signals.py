from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
#from django.contrib.auth.models import User
from .models import User_settings,Subscriber

from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_save, sender=User)
def change_activity_status(sender, instance,created, **kwargs):
    """ Signal to activate the profile (if the email and phone number are confirmed) """
    try:
        if created:
            User_settings.objects.create(user=instance)
            #Subscriber.objects.create(user=instance)

        # profile = User_settings.objects.get(user_prf=instance)
        # instance.is_active = True
        # instance.save()
        # if profile.confirm_email and profile.confirm_phone_num == True:
        #     instance.is_active = True
        #     instance.save()
    except User_settings.DoesNotExist:
        pass

#
#
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         User_settings.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()