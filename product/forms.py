from django import forms

class ProductSearchForm(forms.Form):
    name = forms.CharField(required=False)
    price = forms.FloatField(required=False)
    category = forms.CharField(required = False)