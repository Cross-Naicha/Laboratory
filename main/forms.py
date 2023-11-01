from django import forms

# Create your forms here:
class Patient(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    height = forms.FloatField()
    weight = forms.FloatField()
    bloodGlucose = forms.FloatField()
    triglycerides = forms.FloatField()