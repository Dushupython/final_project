from django.contrib import admin

# Register your models here.
from .models import Bitcoin, Symbol

admin.site.register(Bitcoin)
admin.site.register(Symbol)
