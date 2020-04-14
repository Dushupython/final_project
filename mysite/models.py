from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.
import datetime
from mysite.price_com import price


class Bitcoin(models.Model):
    trigger_price = models.IntegerField(
        verbose_name='Триггер'
    )

    def get_absolute_url(self):
        return reverse('mysite:index')


from mysite.signals import Alert

post_save.connect(Alert, sender=Bitcoin)


class Symbol(models.Model):
    symbol = models.CharField(
        max_length=256
    )
    price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=15,
        decimal_places=10,
    )
    last_update = models.DateTimeField()

    def get_latest_data(self):
        if (datetime.datetime.now().replace(tzinfo=None) - self.last_update.replace(tzinfo=None)).total_seconds() > 10:
            self.update_data()
        return self.price

    def update_data(self):
        new_data = price(self.symbol)
        self.price = new_data.get('price')
        self.last_update = datetime.datetime.now()
        self.save()


