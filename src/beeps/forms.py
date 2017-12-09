from django import forms
from .models import Beep

class BeepModelForm(forms.ModelForm):
    class Meta:
        model = Beep
        fields = [
            'content'
        ]