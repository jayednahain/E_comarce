from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(forms.Form):
   username = forms.CharField()
   email    = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput)
   password2 = forms.CharField(label='confirm password: ',widget=forms.PasswordInput)


   #check user name is alrady exist or not
   def clean_username(self):
      username = self.cleaned_data.get('username')
      print(username)
      qs = User.objects.filter(username=username)

      if qs.exists():
         raise forms.ValidationError('User name is alrady taken')

      return username

   #checking email already have or not
   def clean_email(self):
      username = self.cleaned_data.get('username')
      print(username)
      qs = User.objects.filter(username=username)

      if qs.exists():
         raise forms.ValidationError('User email is already taken')

      return username

   #two password matchi8ng confermation
   def clean(self):
      data = self.cleaned_data
      password = self.cleaned_data.get('password')
      password2 = self.cleaned_data.get('password2')

      if password2 != password:
         raise forms.ValidationError('password Must match! ')
      return data
