from Utility_Tools.Order_id_genarator import Unique_order_id_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from Order_product.models import Order



@receiver(pre_save, sender=Order)
def product_order_id_pre_save(sender,instance,*args,**kwargs):
   if not instance.order_id:
      instance.order_id = Unique_order_id_generator(instance)






