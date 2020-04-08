from django.contrib.sites import requests
from django.shortcuts import render
from mysite.price_com import symbol, price
import requests
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import BitcoinForm
from .models import Bitcoin
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
