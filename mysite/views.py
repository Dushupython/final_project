from django.contrib.sites import requests
from django.shortcuts import render
from mysite.price_com import symbol, price
import requests
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView
from .forms import BitcoinForm
from .models import Bitcoin, Symbol
from django.template import Context
from .compare import price

# def btc_usd(request):
#     return HttpResponse(price('BTCUSDT'))


# def index(request):
#     data = {"price": price('BTCUSDT'), "price_1": price('ETHUSDT')}
#     return render(request, 'mysite/base.html', context=data)


class CreateBitcoinAlert(CreateView):
    model = Bitcoin
    template_name = 'mysite/trigger.html'
    form_class = BitcoinForm


def get_latest_data(symbols: tuple):
    symbols = Symbol.objects.filter(symbol__in=symbols)
    data = {f'price_{i}': symbol.get_latest_data() for i, symbol in enumerate(symbols)}
    return data


def index(request):
    data = get_latest_data(('BTCUSDT', 'ETHUSDT'))
    return render(request, 'mysite/base.html', context=data)


def get_data_use_axios(request):
    data = get_latest_data(('BTCUSDT'))
    return JsonResponse(data)