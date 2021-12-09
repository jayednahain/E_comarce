from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView
from product.models import Porduct


"""if there is same name in slug filed this will be userd"""
class ProductDetailSLUGview(DetailView):
   queryset = Porduct.objects.all()
   template_name = 'slug_view.html'
   def get_context_data(self, *args, object_list=None, **kwargs):
      context = super(ProductDetailSLUGview, self).get_context_data(*args,**kwargs)
      print(context)
      return context
   def get_object(self, *args,**kwargs):
      request = self.request
      slug = self.kwargs.get('slug')

      try:
         instance = Porduct.objects.get(slug=slug,featured=True)
      except Porduct.DoesNotExist:
         raise Http404('Custom error ! no product found')
      except Porduct.MultipleObjectsReturned:
         query_set = Porduct.objects.filter(slug=slug,featured=True)
         instance = query_set.first()
      return instance
