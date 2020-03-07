from django import forms
from .models import Bitcoin


class BitcoinForm(forms.ModelForm):
    class Meta:
        model = Bitcoin
        fields = '__all__'
