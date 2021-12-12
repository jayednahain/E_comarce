
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('User.urls')),
    path('admin/', admin.site.urls),
    path('product/',include(('product.urls','product'),namespace='product')),
    path('search/',include(('search.urls','search'),namespace='search')),
    path('cart',include(('shopping_Cart.urls','shopping_Cart'),namespace='shopping_Cart')),


    path('test/',include('Tags.urls'))

]

#if debug == True
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


