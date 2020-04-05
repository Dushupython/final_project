from .models import Bitcoin
from mysite.compare import comparison


def Alert(sender: Bitcoin, instance: Bitcoin, **kwargs):
    trigger_price = instance.trigger_price
    comparison(trigger_price)

