from django.shortcuts import render

from django.shortcuts import render, redirect
from User.custom_forms.LoginForm import LoginForm
from User.custom_forms.RegisterForm import RegisterForm
from User.custom_forms.ContactForm import ContactForm
from django.contrib.auth import authenticate, login, get_user_model

#8.8
# urls
from django.utils.http import is_safe_url


# Create your views here.


def home_page(request):
   return render(request, 'home.html')


def login_page(request):
   form = LoginForm(request.POST or None)
   context = {
      'form': form
   }

   #url
   #8.8
   #log in form any where and redirect current page!
   next_get_request = request.GET.get('next')
   next_post_request = request.POST.get('next')
   redirect_path = next_get_request or next_post_request or None


   if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         context['form'] = LoginForm()
         if is_safe_url(redirect_path,request.get_host()):
            print("short log in run!")
            return redirect(redirect_path)
         else:
            return redirect('home_page_link')
      else:
         print("error in log in")

   return render(request, 'log_in.html', context)


User = get_user_model()


# get user model will help us for creating new user
def register_page(request):
   form = RegisterForm(request.POST or None)
   context = {
      'form': form
   }
   if form.is_valid():
      username = form.cleaned_data.get("username")
      email = form.cleaned_data.get("email")
      password = form.cleaned_data.get("password")
      new_user = User.objects.create_user(username, email, password)
   return render(request, 'registration.html', context)


def contact_django_form(request):
   form = ContactForm(request.POST or None)
   full_name = request.POST.get('full_name')
   email = request.POST.get('email')
   content = request.POST.get('content')
   print(full_name)
   print(content)
   if form.is_valid():
      # after submit if the data is still on the field
      print(form.cleaned_data)
   return render(request, 'contact.html', {'form': form})
