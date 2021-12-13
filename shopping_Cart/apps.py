from django.apps import AppConfig


class ShoppingCartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_Cart'


class shoopting_cart_SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_Cart'
    def ready(self):
        from shopping_Cart.Custom_signals import cart_total_price_m2m