from django.shortcuts import render
from shopping_Cart.models import Cart

# Create your views here.


"""
Case One:
   1.Getting current cart_id form session
   2.Filter on Cart model with the cart_id
   3.if this already exists then close
   4.if this the session cart_id is empty
      5.getting the current user
         6.not checking the current session have any user or not
      7.create new cart with the current user
      8. finally adding the current cart_id as a session id
      
   code::
   
   def chart(request):
      cart_id = request.session.get('cart_id', None)
      query_set = Cart.objects.filter(id=cart_id)
      if query_set.count() == 1:
         print("this cart already exists")
         cart_obj = query_set.first()
      else:
         print(request.user)
         cart_obj = Cart.objects.new_cart(user=request.user)
         request.session['cart_id'] = cart_obj.id
      return render(request, 'chart.html')
"""


def chart(request):
   # request.session['cart_id']="12"
   cart_id = request.session.get('cart_id', None)
   query_set = Cart.objects.filter(id=cart_id)
   if query_set.count() == 1:
      print("this cart already exists")
      cart_obj = query_set.first()

      #if that cart is exist without any user!,
      #if will update the user
      if request.user.is_authenticated and cart_obj.user is None:
         cart_obj.user = request.user
         cart_obj.save()
   else:
      print(request.user)
      cart_obj = Cart.objects.new_cart(user=request.user)
      request.session['cart_id'] = cart_obj.id

   return render(request, 'chart.html')
