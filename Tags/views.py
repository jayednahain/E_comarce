from django.shortcuts import render
from Tags.models import Tag
from product.models import Porduct


# Create your views here.
def test_data(request):
   # forward search
   # tag > product
   tag_object = Tag.objects.all()
   tag_instace = tag_object.last()
   product_list = tag_instace.product.all()
   product_instance = product_list.first()

   # reverce search

   """in product table we have nothing to access in tag table"""
   product_object = Porduct.objects.all()
   product_table_instance = product_object.first()

   """access tag list using tag set"""
   tag_data = product_table_instance.tag_set.all()
   print()

   contenx = {
      'tag_object': tag_object,
      'tag_instace': tag_instace,
      'product_list': product_list,
      'product_instance': product_instance,
      'product_object': product_object,
      'product_table_instance': product_table_instance,
      'tag_data':tag_data

   }
   return render(request, 'Explore_many_to_many_data.html', contenx)
