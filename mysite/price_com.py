import requests


BASE_URL = f'https://api.binance.com/api/v3/ticker/price?symbol='


def symbol(sym: str):
    return BASE_URL + sym


def price(pair: str):
    price = requests.get(symbol(pair)).json()
    price = price.get('price')
    return price
