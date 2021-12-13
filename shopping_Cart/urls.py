from django.urls import path,include
from shopping_Cart.views import chart,update_cart

urlpatterns = [
    path('',chart,name='chart_home_link'),
    path('update',update_cart,name='update_cart_link')
]
