from django.apps import AppConfig


class SpamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spam'
    def ready(self):
        import spam.signals  # noqa

