from django.urls import path
from User import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',views.home_page,name='home_page_link'),
    path('login',views.login_page,name='login_link'),
    path('registation',views.register_page,name='registation_page_link'),
    path('contact',views.contact_django_form,name='contact_link'),
    path('logout',LogoutView.as_view(),name='logout_link')
]