from django.conf import settings
from django.db import models
from product.models import Porduct
from shopping_Cart.custom_cart_manager import CartManager
# Create your models here.

User = settings.AUTH_USER_MODEL



# class CartManager(models.Manager):
#    def new_or_get(self,request):
#       cart_id = request.session.get("cart_id", None)
#       qs = self.get_queryset().filter(id=cart_id)
#       if qs.count() == 1:
#          #new
#          new_obj= False
#          print('card ID exists')
#          cart_obj = qs.first()
#          if request.user.is_authenticated and cart_obj.user is None:
#             cart_obj.user = request.user
#             cart_obj.save()
#       else:
#          cart_obj = Cart.objects.new_cart(user=request.user)
#          #new
#          new_obj =True
#          request.session['cart_id'] = cart_obj.id
#       return cart_obj,new_obj
#    def new_cart(self,user=None):
#       user_obj = None
#       if user is not None:
#          if user.is_authenticated:
#             user_obj=user
#       return self.model.objects.create(user=user_obj)

class Cart(models.Model):
   user         = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
   product      = models.ManyToManyField(Porduct,blank=True) #one user can multiple product in chart
   total        = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
   updated      = models.DateTimeField(auto_now=True)
   created_time = models.DateTimeField(auto_now_add=True)
   objects      = CartManager()

   def __str__(self):
      return str(self.id)

