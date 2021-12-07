from django.db.models.signals import pre_save,post_save
from product.models import Porduct
from product.Utilities.slug_generator import unique_slug_generator
from django.dispatch import receiver


@receiver(pre_save, sender=Porduct)
def product_slug_pre_save(sender,instance,*args,**kwargs):
   print(" Slug signal run! ")
   if not instance.slug:
      instance.slug = unique_slug_generator(instance)