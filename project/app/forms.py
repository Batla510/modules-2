from django import forms

class AddMen(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(min_value=0)
