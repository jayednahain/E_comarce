from django.http import Http404
from django.shortcuts import render, get_object_or_404
from product.models import Porduct


def home_view(request):
   return render(request,'FunctionBasedView/welcome_page.html')


def product_list(request):
   queryset = Porduct.objects.all()
   context = {
      'object_list':queryset
   }
   return render(request,'FunctionBasedView/list_view.html',context)

# def detail_view(request,*args,**kwargs):
#    pk = kwargs['pk']
#    print(pk)
#    """query set retrun object"""
#    #queryset = Porduct.objects.all()
#    """for single product it will be instance"""
#    instance = get_object_or_404(Porduct,pk=pk)
#    context = {
#       'object': instance
#    }
#    return render(request,'FunctionBasedView/detail_view.html',context)


"""using try block"""
# def detail_view(request,*args,**kwargs):
#
#    try:
#       pk = kwargs['pk']
#       instance = Porduct.objects.get(pk=pk)
#    except Porduct.DoesNotExist:
#       print("No product found")
#    context = {
#       'object': instance
#    }
#    return render(request,'FunctionBasedView/detail_view.html',context)

"""get 404 eror in try block"""

# def detail_view(request,*args,**kwargs):
#    try:
#       pk = kwargs['pk']
#       instance = Porduct.objects.get(pk=pk)
#    except Porduct.DoesNotExist:
#       print("No product found")
#       raise Http404("Cusom err0r !")
#    context = {
#       'object': instance
#    }
#    return render(request,'FunctionBasedView/detail_view.html',context)


"""using exists"""


def detail_view(request,*args,**kwargs):
   pk = kwargs['pk']
   query_set = Porduct.objects.filter(id=pk)
   if query_set.exists() and query_set.count()==1:
      instance = query_set.first()

   context = {
         'object': instance
      }

   return render(request,'FunctionBasedView/detail_view.html',context)

