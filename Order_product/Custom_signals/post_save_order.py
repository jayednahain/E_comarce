from django.db.models.signals import post_save
from django.dispatch import receiver
from Order_product.models import Order





@receiver(post_save, sender=Order)
def post_save_order(sender,instance,created,*args,**kwargs):
   if created:
      print("save_order_run")
      instance.update_total()