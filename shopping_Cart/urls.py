from django.urls import path,include
from shopping_Cart.views import chart,update_cart,check_out_view

urlpatterns = [
    path('',chart,name='chart_home_link'),
    path('update',update_cart,name='update_cart_link'),
    path('checkout',check_out_view,name='check_out_link')
]
