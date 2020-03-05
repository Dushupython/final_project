from django.contrib.sites import requests
from django.shortcuts import render
from mysite.request_price import symbol
import requests


def index(request):
    btc_price = requests.get(symbol('BTCUSDT')).text
    return render(request, 'mysite/index.html', context={'btc_price': btc_price})
