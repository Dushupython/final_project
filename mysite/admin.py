from django.contrib import admin

# Register your models here.
from .models import Trigger, Symbol

admin.site.register(Trigger)
admin.site.register(Symbol)
