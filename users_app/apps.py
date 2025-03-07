from django.apps import AppConfig
from django.db.models.signals import post_save

class UsersAppConfig(AppConfig):
    name = 'users_app'

    def ready(self):
        from users_app.signals import create_profile
        from django.contrib.auth.models import User
        post_save.connect(create_profile, sender=User)
