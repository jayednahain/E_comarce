from search.views import SearchProductView


from django.urls import path

urlpatterns = [
    path('SearchList',SearchProductView.as_view(),name='search_product_link')
]