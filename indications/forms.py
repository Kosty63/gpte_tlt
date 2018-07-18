from django import forms
from .models import *

class IndicationsForm(forms.ModelForm):
    class Meta:
        model = IndicationsModel
        exclude = [""]

