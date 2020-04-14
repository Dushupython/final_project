from django.urls import path
from .views import index, get_data_use_axios
from .views import CreateBitcoinAlert

app_name = 'mysite'
urlpatterns = [
    path('', index, name='index'),
    path('trigger/', CreateBitcoinAlert.as_view(), name='trigger'),
    path('get_data/', get_data_use_axios, name='for_axios')
]
