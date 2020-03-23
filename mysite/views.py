from django.contrib.sites import requests
from django.shortcuts import render
from mysite.price_com import symbol, price
import requests
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import BitcoinForm
from .models import Bitcoin


def index(request):
    return HttpResponse(price('BTCUSDT'))


class CreateBitcoinAlert(CreateView):
    model = Bitcoin
    template_name = 'mysite/trigger.html'
    form_class = BitcoinForm
