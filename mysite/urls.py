from django.urls import path
from .views import index
from .views import CreateBitcoinAlert

app_name = 'mysite'
urlpatterns = [
    path('', index, name='index'),
    path('trigger/', CreateBitcoinAlert.as_view(), name='bitcoin_form')
]
