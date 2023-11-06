from django import forms

class Patients_Blueprint(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    weight = forms.CharField(max_length=10)
    height = forms.FloatField()
    bloodGlucose = forms.FloatField()
    triglycerides = forms.FloatField()

class Patients_Create(Patients_Blueprint):
    ...

class Patients_Modify(Patients_Blueprint):
    ...