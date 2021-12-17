from django.apps import AppConfig

class OrderProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Order_product'


class Order_Product_signals_config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Order_product'
    def ready(self):
        from Order_product.Custom_signals import product_order_id_pre_save
        from Order_product.Custom_signals import post_save_order
        from Order_product.Custom_signals import post_save_card_total