from django.http import Http404
from django.views.generic import ListView,DetailView,TemplateView
from product.models import Porduct




class List(ListView):
   queryset = Porduct.objects.all()
   template_name = 'main/list.html'



class Detail(DetailView):
   queryset = Porduct.objects.all()
   template_name = 'main/detail.html'
   def get_context_data(self, *args, object_list=None, **kwargs):
      context = super(Detail, self).get_context_data(*args,**kwargs)
      #context['view_brand_name'] = 'Ecomarce site from view'
      print(context)
      return context

   def get_object(self, *args,**kwargs):
      request = self.request
      slug = self.kwargs.get('slug')


      """all the slug field are unique if same name in multiple filed"""
      try:
         instance = Porduct.objects.get(slug=slug)
         #instance = Porduct.objects.get_by_id(pk)
      except Porduct.DoesNotExist:
         raise Http404('Custom error ! no product found')
      except Porduct.MultipleObjectsReturned:
         query_set = Porduct.objects.filter(slug=slug)
         instance = query_set.first()
      return instance