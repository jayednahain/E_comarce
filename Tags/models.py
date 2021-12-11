from django.db import models
from product.models import Porduct

class Tag(models.Model):
   title         = models.CharField(max_length=30)
   slug         = models.SlugField(max_length=30)
   created_time = models.DateTimeField(auto_now_add=True)
   tag_active   = models.BooleanField(default=True)
   product      = models.ManyToManyField(Porduct,blank=True)

   def __str__(self):
      return self.title




