from django.conf import settings
from django.db import models
from product.models import Porduct
from shopping_Cart.custom_manager import CartManager
# Create your models here.

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
   user         = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
   product      = models.ManyToManyField(Porduct,blank=True) #one user can multiple product in chart
   total        = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
   updated      = models.DateTimeField(auto_now=True)
   created_time = models.DateTimeField(auto_now_add=True)

   objects      = CartManager()


   def __str__(self):
      return str(self.id)

