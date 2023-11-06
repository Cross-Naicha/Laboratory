from django import forms


class Doctors_Create(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)