from django.contrib.sites import requests
from django.shortcuts import render
from mysite.request_price import symbol
import requests
from django.http import HttpResponse


def index(request):
    btc_price = requests.get(symbol('BTCUSDT')).text
    return HttpResponse(btc_price)
