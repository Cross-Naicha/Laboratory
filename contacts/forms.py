from django import forms

class Suscriptors_Create(forms.Form):
    email = forms.CharField(max_length=30)