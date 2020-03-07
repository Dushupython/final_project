import requests

BASE_URL = f'https://api.binance.com/api/v3/ticker/price?symbol='


def symbol(sym: str):
    return BASE_URL + sym

