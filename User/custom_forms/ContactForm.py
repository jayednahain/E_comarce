from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class ContactForm(forms.Form):
   full_name = forms.CharField(
      label="",
      widget=forms.TextInput(attrs={
         'class':'form-control',
         'placeholder':'type full name',
         'id':'full_name_id'
      }
      )
   )
   email = forms.EmailField(label="",
      widget=forms.EmailInput(attrs={
         'class': 'form-control',
         'placeholder': 'type Email',
         'id':'email_id'
      }
      )
   )
   content   = forms.CharField(
      label="",
      widget=forms.Textarea(attrs={
         'class': 'form-control',
         'placeholder': 'type full content',
         'id':'content_id'
      }
      )
   )

   #custom error for email

   #error

   def clean_email(self):
      email = self.cleaned_data.get('email')
      print("custom validation for email RUN !!!")

      if not "@gmail.com" in email:
         raise forms.ValidationError("Email has to be gmail")

      return email

   def clean_content(self):

      print("content validation run")
      content = self.cleaned_data.get('content')
      print(len(content))
      if len(content) < 10:
         raise forms.ValidationError(f'Please write some more content, {len(content)} is not enough')
      else:
         pass