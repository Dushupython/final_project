from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='user_profile'
    )
    id = models.AutoField(
        verbose_name='id',
        primary_key=True,

    )

    # def __getattribute__(self, name):
    #
    #     if name == 'telegram_id':
    #         return self.telegram_id
    #
    #     else:
    #         return object.__getattribute__(self, name)
    def __str__(self):
        print(self.__getattribute__('telegram_id'))
        return f'{self.user.username} {self.user.email}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = (
            'id',
        )
