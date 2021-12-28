from django.db import models
from Gust_user.models import GustUser





class BillingProfileManager(models.Manager):
   def new_or_get_billing_profile(self,request):
      user = request.user
      gust_user_id = request.session.get('gust_user_id', None)
      billing_profile =None
      billing_profile_data_created =False


      if user.is_authenticated:
         """logged in user checkout"""

         billing_profile, billing_profile_data_created = self.model.objects.get_or_create(
            user=user, email=user.email
         )
         """gust user checkout"""
      elif gust_user_id is not None:
         gust_user_obj = GustUser.objects.get(id=gust_user_id)
         billing_profile, billing_profile_data_created = self.model.objects.get_or_create(
            email=gust_user_obj.email
         )
      else:
         pass
      return billing_profile,billing_profile_data_created
