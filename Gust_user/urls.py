from django.urls import path,include
from Gust_user.views import gust_user_register
urlpatterns = [
    path('register',gust_user_register,name='gust_register_link')

]