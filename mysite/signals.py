from .models import Bitcoin
from mysite.compare import comparison


def Alert(sender: Bitcoin, instance: Bitcoin, **kwargs):
    # trigger_price = float(sender.objects.values('trigger_price'))
    # comparison(trigger_price)
    # last_element = sender.objects.get('trigger_price')
    trigger_price = instance.trigger_price
    comparison(trigger_price)
    print(last_element)
