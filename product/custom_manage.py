from django.db import models

# class Product_manager(models.Manager):
#    def Get_by_id(self):
#       query_set = self.get_queryset().filter(id=id)  #Product.object == self.get_queryset()


class Product_manager(models.Manager):
   def get_by_id(self,id):
      query_set = self.get_queryset().filter(id=id)  #Product.object == self.get_queryset()
      if query_set.count()==1:
         return query_set.first()
      else:
         None
