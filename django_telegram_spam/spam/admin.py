from django.contrib import admin
from .models import *

admin.site.register(Subscriber)
admin.site.register(User_settings)

# class NewsContentAdmin(admin.ModelAdmin):
#     exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений
#
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.author = request.user
#         super().save_model(request, obj, form, change)
#admin.site.register(Hotel)
#
# class Subscriberadmin (admin.ModelAdmin):
#     class Meta:
#         model = Subscriber

# class ExampleModeladmin (admin.ModelAdmin):
#     class Meta:
#         model = Hotel
