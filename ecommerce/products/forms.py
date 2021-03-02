from django import forms
from .models import Person
from django.forms import ModelForm


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.FloatField()


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'   # for all fields