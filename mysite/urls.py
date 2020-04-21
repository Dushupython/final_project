from django.urls import path
from .views import get_data_use_axios, index
from .views import (CreateTrigger,
                    TriggerListView,
                    DeleteTriggerView,
                    UpdateTriggerView,
                    IndexView
                    )

app_name = 'mysite'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('trigger/', CreateTrigger.as_view(), name='trigger'),
    path('get_data/', get_data_use_axios, name='for_axios'),
    path('trigger_list/', TriggerListView.as_view(), name='trigger_list'),
    path('delete_trigger/<int:pk>', DeleteTriggerView.as_view(), name='delete_trigger'),
    path('update_trigger/<int:pk>', UpdateTriggerView.as_view(), name='update_trigger')
]
