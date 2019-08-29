from django import forms
from .models import Category
from django.forms import ModelForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','url','description','parentid','summary']