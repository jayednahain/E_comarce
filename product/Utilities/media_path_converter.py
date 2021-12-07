import os
import random

def get_filename(filepath):
   base_name      = os.path.basename(filepath)
   name,extension = os.path.splitext(base_name)
   return name,extension


def upload_image_path(instance,filename):

   new_filename   = random.randint(1,34545465)
   name,extension = get_filename(filename)
   final_filename = f'{new_filename}{extension}'.format(new_filename=new_filename,extension=extension)
   return f'Porduct_image/{new_filename}/{final_filename}'.format(
      new_filename=new_filename,
      final_filename=final_filename
   )
