from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.views.generic import ListView

# Create your models here.

class Bitcoin(models.Model):
    trigger_price = models.IntegerField(
        verbose_name='Триггер'
    )

    def get_absolute_url(self):
        return reverse('mysite:index')


from mysite.signals import Alert

post_save.connect(Alert, sender=Bitcoin)


class Price_List_View(ListView):
    template_name = 'mysite/base.html'
    model = Btc_price
