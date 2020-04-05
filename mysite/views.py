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

from django.conf import settings

from django_telegram_login.widgets.constants import (
    SMALL,
    MEDIUM,
    LARGE,
    DISABLE_USER_PHOTO,
)
from django_telegram_login.widgets.generator import (
    create_callback_login_widget,
    create_redirect_login_widget,
)


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

telegram_login_widget = create_callback_login_widget(bot_name, corner_radius=10, size=MEDIUM)

telegram_login_widget = create_redirect_login_widget(
    redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
)

def callback(request):
    telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'mysite/base.html', context)