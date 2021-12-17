from Utility_Tools.random_string_genarator import random_string_generator
from  Utility_Tools.slug_generator import unique_slug_generator

def Unique_order_id_generator(instance):
   order_new_id = random_string_generator()
   model_class = instance.__class__
   check_order_id_query_set = model_class.objects.filter(order_id = order_new_id).exists()
   if check_order_id_query_set:
      print("send for check")
      return unique_slug_generator(instance)
   else:
      print("new_order_id genarated")
      print(order_new_id)
      return order_new_id

