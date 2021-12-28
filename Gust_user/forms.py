from django import forms


class GustUserForm(forms.Form):
   email = forms.CharField()
