from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.
import datetime
from mysite.price_com import price


# class Bitcoin(models.Model):
#     trigger_price = models.IntegerField(
#         verbose_name='Триггер'
#     )
#     pair = models.ForeignKey
#
#     def get_absolute_url(self):
#         return reverse('mysite:index')


# from mysite.signals import Alert
#
# post_save.connect(Alert, sender=Bitcoin)


class Symbol(models.Model):
    symbol = models.CharField(
        max_length=256
    )
    price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=15,
        decimal_places=2,
    )
    last_update = models.DateTimeField()
    pic_link = models.CharField(
        max_length=1024,
        null=True,
        blank=True
    )

    def get_latest_data(self):
        if (datetime.datetime.now().replace(tzinfo=None) - self.last_update.replace(tzinfo=None)).total_seconds() > 5:
            self.update_data()
        return self.price, self.pic_link

    def update_data(self):
        new_data = price(self.symbol)
        new_data = float(new_data.get('price'))
        new_data = float('{:.3f}'.format(new_data))
        self.price = new_data
        self.last_update = datetime.datetime.now()
        self.save()

    def __str__(self):
        return f'{self.symbol}'


class Trigger(models.Model):
    trigger_price = models.IntegerField(
        verbose_name='Price Alert'
    )
    pair = models.ForeignKey(
        Symbol,
        on_delete=models.DO_NOTHING,
        null=True,
        verbose_name='pair'
    )
    telegram_id = models.IntegerField(
        verbose_name='telegram_id',
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('mysite:index')

    def __str__(self):
        return f'{self.trigger_price} {self.pair}'


from mysite.signals import Alert

post_save.connect(Alert, sender=Trigger)
