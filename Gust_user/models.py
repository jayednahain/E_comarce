from django.db import models

# Create your models here.
class GustUser(models.Model):
   email = models.EmailField()
   active = models.BooleanField(default=True)
   updated_time = models.DateTimeField(auto_now=True)
   created_time = models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return self.email