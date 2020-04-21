from django.contrib.sites import requests
from django.shortcuts import render
from mysite.price_com import symbol, price
import requests
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .forms import TriggerForm
from .models import Trigger, Symbol
from django.template import Context
from .compare import price
from django.urls import reverse_lazy, reverse


class CreateTrigger(CreateView):
    model = Trigger
    template_name = 'mysite/trigger.html'
    form_class = TriggerForm


class TriggerListView(ListView):
    model = Trigger
    template_name = 'mysite/trigger_list.html'
    context_object_name = 'trigger_list'


class UpdateTriggerView(UpdateView):
    model = Trigger
    template_name = 'mysite/trigger.html'
    form_class = TriggerForm


class DeleteTriggerView(DeleteView):
    template_name = 'mysite/confirm_delete.html'
    model = Trigger
    success_url = reverse_lazy('mysite:trigger_list')


def get_latest_data(symbols: tuple):
    symbols = Symbol.objects.filter(symbol__in=symbols)
    data = {f'{symbol.symbol}': symbol.get_latest_data() for symbol in symbols}
    return data


def index(request):
    return render(request, 'mysite/base.html', context=None)


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users_app:login')
    template_name = 'mysite/base.html'


def get_data_use_axios(request):
    data = get_latest_data(('BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'XRPUSDT', 'XMRUSDT', 'ZECUSDT'))
    return JsonResponse(data)
