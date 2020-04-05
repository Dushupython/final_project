from mysite.price_com import symbol, price
import requests
import telepot
import time

token = '1131352838:AAEY9zWfKDhLym85jHj5iylnyU4Wzf3YwqA'
TelegramBot = telepot.Bot(token)


def comparison(trigger_price_1: float):
    if trigger_price_1 < float(price('BTCUSDT')):
        up(trigger_price_1)
    else:
        down(trigger_price_1)


def up(trigger_price_1: float):
    if trigger_price_1 >= float(price('BTCUSDT')):
        TelegramBot.sendMessage(623458076, 'Цена BTC/USD достигла отметки ' + str(trigger_price_1))
    else:
        time.sleep(10)
        return up(trigger_price_1)


def down(trigger_price_1: float):
    if trigger_price_1 <= float(price('BTCUSDT')):
        TelegramBot.sendMessage(623458076, 'Цена BTC/USD достигла отметки ' + str(trigger_price_1))
    else:
        time.sleep(10)
        return down(trigger_price_1)
