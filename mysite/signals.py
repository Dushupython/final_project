from .models import Trigger, Symbol
from mysite.compare import comparison


def Alert(sender: Trigger, instance: Trigger, **kwargs):
    trigger_price = instance.trigger_price
    data = instance.pair.symbol
    telegram_id = instance.telegram_id
    comparison(trigger_price, data, telegram_id)

