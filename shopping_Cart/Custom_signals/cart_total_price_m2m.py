from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from shopping_Cart.models import Cart


@receiver(m2m_changed, sender=Cart.product.through)
def cart_m2m_total_price_revier(sender,instance,action,*args,**kwargs):
   if action == 'pre_remove' or action == 'post_add' or action == 'post_clear':
      print(action)
      # geting all the selected price product
      cart_product = instance.product.all()
      total_price = 0
      for x in cart_product:
         total_price = total_price + x.price
      print(total_price)


      print(cart_product)