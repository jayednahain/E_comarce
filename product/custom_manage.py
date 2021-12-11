from django.db import models
from django.db.models import Q

# class Product_manager(models.Manager):
#    def Get_by_id(self):
#       query_set = self.get_queryset().filter(id=id)  #Product.object == self.get_queryset()


"""we can use custom query from manager
   While we can just access it just in object !
   -----
   if we want use it as a custom query set
   
"""


# custom query set
class ProductQuerySet(models.query.QuerySet):
   def featured_data(self):
      return self.filter(featured=True)

   def active_data(self):
      return self.filter(active_prduct=True)

   def search_data(self, query):
      DB_QUERY = Q(title__icontains=query) | \
                 Q(description__icontains=query)|\
                 Q(price__icontains=query)|\
                 Q(tag__title__icontains=query)
      return self.filter(DB_QUERY).distinct()


class Product_manager(models.Manager):
   def get_queryset(self):
      return ProductQuerySet(self.model, using=self._db)

   # over write all query
   def all(self):
      return self.get_queryset().active_data()

   # custom query
   def get_by_id(self, id):
      query_set = self.get_queryset().filter(id=id)  # Product.object == self.get_queryset()
      if query_set.count() == 1:
         return query_set.first()
      else:
         None

   def get_featured_items(self):
      return self.get_queryset().featured_data()


   def get_search_items(self,query):
      return self.get_queryset().active_data().search_data(query)
