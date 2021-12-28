from django.db import models




#13
class Order_manager(models.Manager):

   def new_or_get_order(self,billing_profile,cart_obj):
      order_obj_created = False
      qs = self.get_queryset().filter(
         billing_profile=billing_profile,
         cart=cart_obj,
         active=True)
      if qs.count() == 1:
         order_obj_created = False
         obj = qs.first()
      else:
         obj = self.model.objects.create(
            billing_profile=billing_profile,
            cart=cart_obj)
         order_obj_created = True
      return obj,order_obj_created
