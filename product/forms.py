from django import forms

""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ This is a model to create a form that will be used/validated in a view   │
  │ model                                                                    │
  └──────────────────────────────────────────────────────────────────────────┘
 """
class ProductSearchForm(forms.Form):
    name = forms.CharField(required=False)
    price = forms.FloatField(required=False)
    category = forms.CharField(required = False)