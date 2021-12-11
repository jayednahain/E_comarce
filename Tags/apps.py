from django.apps import AppConfig


class TagsConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'Tags'


class TagSignalsConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'Tags'

   def ready(self):
      from Tags.Tag_singnals.Slug_generator_pre_save import tag_slug_pre_save
