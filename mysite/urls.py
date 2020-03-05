from django.urls import path
from .views import index

app_name = 'mysite'
urlpatterns = [
    path('', index, name='index')
]
