from django.views.generic import ListView,DetailView,TemplateView
from product.models import Porduct


class ProductFeaturedList(ListView):
   template_name = 'FeaturedProductView/featuredProductList.html'
   def get_queryset(self):
      request = self.request

      #object method
      #return Porduct.objects.get_featured_items()

      #define custom queryset method
      return  Porduct.objects.all().featured()


class ProductFeaturedDetail(DetailView):
   queryset = Porduct.objects.get_featured_items()
   template_name = 'FeaturedProductView/featuredDetail.html'


