from django.shortcuts import render, redirect
from shopping_Cart.models import Cart
from product.models import Porduct
from Order_product.models import Order
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
   cart_obj,new_obj = Cart.objects.new_or_get(request)

   context = {
      'cart':cart_obj
   }
   return render(request, 'chart.html',context)

def update_cart(request):
   #10
   pro_id = request.POST.get('product_id',None)
   #9
   #update cart
   #pro_id = 1
   if pro_id is not None:
      try:
         product_obj = Porduct.objects.get(id = pro_id)
         cart_obj, new_obj = Cart.objects.new_or_get(request)
         if product_obj in cart_obj.product.all():
            cart_obj.product.remove(product_obj)
         else:
            cart_obj.product.add(product_obj)
         request.session['total_cart_product']=cart_obj.product.count()
      except Porduct.DoesNotExist:
         print('product dose not exist')
         return redirect('shopping_Cart:chart_home_link')
   return redirect('shopping_Cart:chart_home_link')

def check_out_view(request):
   cart_obj,new_obj = Cart.objects.new_or_get(request)
   order_obj = None

   if new_obj or cart_obj.product.count()==1:
      return redirect('shopping_Cart:chart_home_link')
   else:
      order_obj,new_order_obj = Order.objects.get_or_create(cart=cart_obj)
   return render(request,'check_out_process.html',{'object':order_obj})

