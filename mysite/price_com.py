import requests
import _sqlite3

BASE_URL = f'https://api.binance.com/api/v3/ticker/price?symbol='


def symbol(sym: str):
    return BASE_URL + sym


def price(pair: str):
    price = requests.get(symbol(pair)).json()
    price = float(price.get('price'))
    return price
