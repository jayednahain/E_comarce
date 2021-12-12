from django.db import models
# from shopping_Cart.models import Cart

#from shopping_Cart.models import C


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
#          cart_obj = .objects.new(user=request.user)
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

