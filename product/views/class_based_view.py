from django.http import Http404
from django.views.generic import ListView,DetailView,TemplateView
from product.models import Porduct

class HomeView(TemplateView):
   template_name = 'classBasedView/welcome_page.html'

class ProductlistView(ListView):
   queryset = Porduct.objects.all()
   template_name = 'classBasedView/list_view.html'

   # def get_context_data(self, *args, object_list=None, **kwargs):
   #    context = super(ProductlistView, self).get_context_data(*args,**kwargs)
   #    print(context)
   #
   #    return context


# class ProductDetailview(DetailView):
#    queryset = Porduct.objects.all()
#    template_name = 'FunctionBasedView/detail_view.html'
#    def get_context_data(self, *args, object_list=None, **kwargs):
#       context = super(ProductDetailview, self).get_context_data(*args,**kwargs)
#       print(context)
#
#       return context


"""detail veiw using get_obejct"""
class ProductDetailview(DetailView):
   #queryset = Porduct.objects.all()
   template_name = 'FunctionBasedView/detail_view.html'
   def get_context_data(self, *args,**kwargs):
      context = super(ProductDetailview,self).get_context_data(*args,**kwargs)
      return context

   def get_object(self,*args,**kwargs):
      request = self.request
      pk = self.kwargs.get('pk')
      instance = Porduct.objects.get_by_id(pk)

      if instance is None:
         raise Http404("custom error product not found!")
      return instance

