from django import forms

class AddToCartForm(forms.Form):
    id = forms.IntegerField()
    quantity = forms.IntegerField()