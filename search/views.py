from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from product.models import Porduct
# Create your views here.


class SearchProductView(ListView):
   template_name = 'search_result_list.html'

   def get_context_data(self, *args, object_list=None, **kwargs):
      context = super(SearchProductView, self).get_context_data(*args,**kwargs)

      search_data = self.request.GET.get('q',None)
      #for se the result we just use {{ query }}
      context['query'] = search_data

      return context




   #using this we can get the data in template {{ request.GET.q }}
   def get_queryset(self):
      request = self.request
      method_dict = request.GET
      query = method_dict.get('q',None)
      print(query)

      if query is not None:
         return Porduct.objects.filter(title__icontains=query)

      return Porduct.objects.get_featured_items() # there is no search items it will return only featured items

