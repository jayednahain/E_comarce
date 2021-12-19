from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from billing_profile.models import Billing_Profile

@receiver(post_save,sender=User)
def user_billing_profile_create_reciver_post_save(sender,instance,created,*args,**kwargs):
   if created and instance.email:
      #email use added with user !
      print(instance.email)
      Billing_Profile.objects.get_or_create(user=instance,email=instance.email)

