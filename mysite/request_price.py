import requests

BASE_URL = f'https://api.binance.com/api/v3/ticker/price?symbol='


def symbol(sym: str):
    return BASE_URL + sym


response = requests.get(symbol('BTCUSDT'))
print(response.text)
