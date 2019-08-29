from django import forms
from django.forms import ModelForm


class StartForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)


    