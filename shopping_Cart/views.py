from django.shortcuts import render, redirect

#database
from shopping_Cart.models import Cart
from product.models import Porduct
from Order_product.models import Order
from billing_profile.models import Billing_Profile
from Gust_user.models import GustUser
#form
from User.custom_forms.LoginForm import LoginForm
from Gust_user.forms import GustUserForm


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
         #nav bar cart count!
         request.session['total_cart_product']=cart_obj.product.count()
      except Porduct.DoesNotExist:
         print('product dose not exist')
         return redirect('shopping_Cart:chart_home_link')
   return redirect('shopping_Cart:chart_home_link')

def check_out_view(request):

   cart_obj,new_obj = Cart.objects.new_or_get(request)
   order_obj = None
   if new_obj or cart_obj.product.count() == 0:
      return redirect('shopping_Cart:chart_home_link')

   """billing Profile"""

   log_in_form = LoginForm(request.POST or None)
   gust_user_form = GustUserForm(request.POST or None)

   #14
   billing_profile,billing_profile_data_created = Billing_Profile.objects.new_or_get_billing_profile(request)

   #12
   if billing_profile is not None:
      order_obj , order_obj_created = Order.objects.new_or_get_order(billing_profile,cart_obj)




   context   = {
      'object': order_obj,
      'billing_profile':billing_profile,
      'log_in_form':log_in_form,
      'gust_user_form':gust_user_form
   }
   return render(request,'check_out_process.html',context)

