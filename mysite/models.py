from django.db import models


# Create your models here.

class Bitcoin(models.Model):
    trigger_price = models.IntegerField(
        max_length=10,
        verbose_name='Триггер'
    )
