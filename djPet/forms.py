from django import forms


class PriceChanger(forms.Form):
    itemID = forms.CharField()
    name = forms.Textarea()
    amount = forms.Textarea()
    price = forms.Textarea()
    partNumber = forms.Textarea()
    minRetPrice = forms.Textarea()
