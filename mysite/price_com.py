import requests
import _sqlite3

BASE_URL = f'https://api.binance.com/api/v3/ticker/price?symbol='


def symbol(sym: str):
    return BASE_URL + sym


def price(pair: str):
    price = requests.get(symbol(pair)).json()
    price = price.get('price')
    return price


# def current_price(pair: str, model: classmethod):
#     data = price(pair)
#     requests.post(model, data)
#
#
# current_price('BTCUSDT', Current_price.current_price_btc)
#
