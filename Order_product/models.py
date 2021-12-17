import decimal

from django.db import models
from shopping_Cart.models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver


ORDER_STATUS_CHOISE = (
   ('created','Created'),
   ('paid','Paid'),
   ('shipped','Shipped'),
   ('refunded','Refunded')
)

# Create your models here.
class Order(models.Model):
   order_id        = models.CharField(max_length=120,blank=True)
   cart            = models.ForeignKey(Cart,on_delete=models.CASCADE)
   order_status    = models.CharField(max_length=50,default='created',choices=ORDER_STATUS_CHOISE)
   shippting_total = models.DecimalField(default=5.00,max_digits=100,decimal_places=2)
   total           = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)

   def __str__(self):
      return self.order_id

   def update_total(self):
      cart_total = self.cart.total
      shippting_total = self.shippting_total
      new_total = decimal.Decimal(cart_total)+decimal.Decimal(shippting_total)
      self.total=decimal.Decimal(new_total)
      self.save()
      return new_total


# @receiver(post_save, sender=Order)
# def post_save_order(sender,instance,created,*args,**kwargs):
#    if created:
#       instance.update_total()