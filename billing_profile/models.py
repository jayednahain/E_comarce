from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Billing_Profile(models.Model):
   user         = models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
   email        = models.EmailField()
   active       = models.BooleanField(default=True)
   update_time  = models.DateTimeField(auto_now=True)
   created_time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.email




