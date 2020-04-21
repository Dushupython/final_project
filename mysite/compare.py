from django.contrib.auth.models import User

from mysite.price_com import symbol, price
import requests
import telepot
import time
from users_app.models import Profile
token = '1131352838:AAEY9zWfKDhLym85jHj5iylnyU4Wzf3YwqA'
TelegramBot = telepot.Bot(token)


def comparison(trigger_price_1: float, data: str, telegram_id: int):
    if trigger_price_1 < float(price(data)['price']):
        up(trigger_price_1, data, telegram_id)
    else:
        down(trigger_price_1, data, telegram_id)


def up(trigger_price_1: float, data: str, telegram_id: int):
    if trigger_price_1 >= float(price(data)['price']):
        TelegramBot.sendMessage(telegram_id, 'Цена ' + str(data) + ' достигла отметки ' + str(trigger_price_1))
    else:
        time.sleep(10)
        return up(trigger_price_1, data, telegram_id)


def down(trigger_price_1: float, data: str, telegram_id):
    if trigger_price_1 <= float(price(data)['price']):
        TelegramBot.sendMessage(telegram_id, 'Цена ' + str(data) + ' достигла отметки ' + str(trigger_price_1))
    else:
        time.sleep(10)
        return down(trigger_price_1, data, telegram_id)
