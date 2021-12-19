from django.apps import AppConfig


class BillingProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing_profile'


class BillingProfileConfig_signals(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing_profile'
    def ready(self):
        from billing_profile.custom_signal.user_billing_profile_create_reciver_post_save import user_billing_profile_create_reciver_post_save