from django.urls import path,include
from shopping_Cart.views import chart


urlpatterns = [
    path('',chart,name='chart_link')
]
