from django.db.models.signals import post_save
from django.dispatch import receiver
from Order_product.models import Order
from shopping_Cart.models import Cart

"""based of cart order total will be generate"""

@receiver(post_save, sender=Cart)
def post_save_card_total(sender,instance,created,*args,**kwargs):
   if not created:
      cart_obj = instance
      cart_total = instance.total
      cart_id = instance.id
      query_set = Order.objects.filter(cart_id=cart_id)
      if query_set.exists() and query_set.count() ==1:
         order_obj = query_set.first()
         order_obj.update_total()
         print("cart_total_run")



