from django import forms

# Create your forms here:

# Pacientes:
class Patients_Create(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    weight = forms.CharField(max_length=10)
    height = forms.FloatField()
    bloodGlucose = forms.FloatField()
    triglycerides = forms.FloatField()

# Medicos:

class Doctors_Create(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)

# Suscriptores:

class Suscriptors_Create(forms.Form):
    email = forms.CharField(max_length=30)