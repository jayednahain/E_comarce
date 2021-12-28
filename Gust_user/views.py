from django.shortcuts import render, redirect
from Gust_user.forms import GustUserForm
from django.utils.http import is_safe_url

#data
from Gust_user.models import GustUser

def gust_user_register(request):
   form = GustUserForm(request.POST or None)
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
      email = form.cleaned_data.get('email')
      new_gust_user = GustUser.objects.create(email=email)
      request.session['gust_user_id'] = new_gust_user.id

      if is_safe_url(redirect_path,request.get_host()):
         return redirect(redirect_path)
      else:
         return redirect('registation_page_link')

   return redirect('registation_page_link')
