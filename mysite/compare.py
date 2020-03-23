from mysite.price_com import symbol, price
import requests
import telepot

token = '1131352838:AAEY9zWfKDhLym85jHj5iylnyU4Wzf3YwqA'
TelegramBot = telepot.Bot(token)


def comparison(trigger_price_1: float):
    if trigger_price_1 >= float(price('BTCUSDT')):
        TelegramBot.sendMessage(623458076, 'Test')
    else:
        pass  # timer
