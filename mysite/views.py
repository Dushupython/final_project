from django.contrib.sites import requests
from django.shortcuts import render
from mysite.request_price import symbol
import requests
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import BitcoinForm
from .models import Bitcoin


def index(request):
    btc_price = requests.get(symbol('BTCUSDT')).text.split('price')
    return HttpResponse(btc_price)


class CreateBitcoinAlert(CreateView):
    model = Bitcoin
    template_name = 'mysite/trigger.html'
    form_class = BitcoinForm
