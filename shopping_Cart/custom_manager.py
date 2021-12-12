from django.db import models


class CartManager(models.Manager):
   def new_cart(self,user=None):
      user_obj = None
      if user is not None:
         if user.is_authenticated:
            user_obj=user
      return self.model.objects.create(user=user_obj)

