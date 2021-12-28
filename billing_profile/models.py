from django.db import models
from django.contrib.auth.models import User

#14
#custom manager
from billing_profile.Custom_manager.custom_manager import BillingProfileManager

"""due to circular import"""






class Billing_Profile(models.Model):
   user         = models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
   email        = models.EmailField()
   active       = models.BooleanField(default=True)
   update_time  = models.DateTimeField(auto_now=True)
   created_time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.email
   #14
   objects     = BillingProfileManager()



