from product.views.function_based_views import home_view,\
    product_list,\
    detail_view
from product.views.class_based_view import HomeView,\
    ProductlistView,\
    ProductDetailview
from product.views.detail_slug_view import ProductDetailSLUGview
from product.views.featuredProduct import ProductFeaturedList,ProductFeaturedDetail

from product.views.main import Detail,List


from django.urls import path

urlpatterns = [

    #main
    #working with only class based views
    path('list/',List.as_view(),name='product_list_link'),
    path('detail/<str:slug>/',Detail.as_view(),name='product_detail_link'),







    #class Based View
    #path('CB_home',HomeView.as_view(),name='cb_home_link'),
    #path('CB_list',ProductlistView.as_view(),name='CB_product_list_link'),
    #path('CB_detail/<int:pk>',ProductDetailview.as_view(),name='CB_product_detail_link'),

    #featured items
    path('CB_featured_list',ProductFeaturedList.as_view(),name='feature_list_link'),
    path('CB_featured_detail/<str:slug>/',ProductFeaturedDetail.as_view(),name='featured_detail_link')


    #slug view
    #path('CB_detail_sulg/<str:slug>', ProductDetailSLUGview.as_view(), name='CB_product_detail_link'),

    #function Based view
    #path('FB_home',home_view, name='fb_home_link'),
    #path('FB_list',product_list,name='fb_list_link'),
    #path('FB_detail/<int:pk>',detail_view,name='fb_product_detail_link')

]
