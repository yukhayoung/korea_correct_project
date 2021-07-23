from django import forms
from .models import Koreaapp

class KoreaappForm(forms.ModelForm):
    class Meta:
        model = Koreaapp
        fields = ['title', 'writer', 'body', 'image']