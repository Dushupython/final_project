from django.apps import AppConfig
from django.db.models.signals import post_save


class MysiteConfig(AppConfig):
    name = 'mysite'

    def ready(self):
        from .signals import Alert
        Bitcoin = self.get_model('Bitcoin')
        post_save.connect(Alert, sender=Bitcoin)
