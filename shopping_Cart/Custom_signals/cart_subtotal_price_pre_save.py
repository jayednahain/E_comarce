from django.db.models.signals import pre_save
from django.dispatch import receiver
from shopping_Cart.models import Cart


@receiver(pre_save, sender=Cart)
def cart_total_price_pre_save_revier(sender,instance,*args,**kwargs):
      if instance.sub_total > 0 :
            instance.total = instance.sub_total*2
      else:
            instance.total = 0.00