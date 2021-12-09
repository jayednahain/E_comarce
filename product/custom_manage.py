from django.db import models

# class Product_manager(models.Manager):
#    def Get_by_id(self):
#       query_set = self.get_queryset().filter(id=id)  #Product.object == self.get_queryset()



"""we can use custom query from manager
   While we can just access it just in object !
   -----
   if we want use it as a custom query set
   
"""
#custom query set
class ProductQuerySet(models.query.QuerySet):
   def featured(self):
      return self.filter(featured=True)


class Product_manager(models.Manager):
   def get_queryset(self):
      return ProductQuerySet(self.model,using=self._db)
   #custom query
   def get_by_id(self,id):
      query_set = self.get_queryset().filter(id=id)  #Product.object == self.get_queryset()
      if query_set.count()==1:
         return query_set.first()
      else:
         None
   #Ccustom query
   def get_featured_items(self):
      return self.get_queryset().filter(featured=True)

