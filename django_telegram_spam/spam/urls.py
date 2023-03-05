from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),]

#path('image_upload', hotel_image_view, name='image_upload'),
urlpatterns = [

    #path('success', success, name='success'),
    path('', views.index),
    path('login/', views.user_login, name='login'),
    path(r'register/', views.register, name='register'),
    path(r'logout/', views.logout_view, name='logout'),
    #path(r'spam_pro/', views.spam_pro, name='spam_pro'),
    path(r'spam_list/<int:id>', views.spam_list, name='spam_list'),
    path(r'spam_pro/', views.spam_pro, name='spam_pro'),
    path('user_settings/<int:id>', views.user_settings, name='user_settings'),
    path('get_wallet/<int:id>', views.get_wallet, name='get_wallet'),
    path('home', views.get_wallet, name='get_wallet'),


    #path(r'user_settings/', views.user_settings, name='user_settings'),


]
#path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
#
# urlpatterns = [
#     path('', views.index),
#     # path('login', views.index),
#     # path('setup_lamp', views.setup_lamp),
#     # path('contact', views.contact),
#     # path('products', views.products),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)