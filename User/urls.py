from django.urls import path
from User import views

urlpatterns = [

    path('',views.home_page,name='home_page_link'),
    path('login',views.login_page,name='login_link'),
    path('registation',views.register_page,name='registation_page_link'),
    path('contact',views.contact_django_form,name='contact_link')

]