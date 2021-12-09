from django.db import models
from product.Utilities.media_path_converter import upload_image_path
from django.urls import reverse

from product.custom_manage import Product_manager
# Create your models here.
class Porduct(models.Model):
   title          = models.CharField(max_length=120)
   description    = models.TextField()
   #12
   slug           = models.SlugField(blank=True,unique=True)
   #12

   featured         = models.BooleanField(default=True)
   price          = models.DecimalField(decimal_places=2,max_digits=20,default=00.00)
   #date = models.DateTimeField(auto_now_add=True)
   product_image = models.ImageField(upload_to=upload_image_path,null=True,blank=False)


   #custom object
   objects = Product_manager()

   def __str__(self):
      return self.title

   def __unicode__(self):
      return self.title

   #12
   def get_absolute_url(self):
      #return 'detail/{slug}/'.format(slug=self.slug)
      return reverse('product:product_detail_link',kwargs={"slug":self.slug})
