from django import forms

# Pacientes:
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

# Medicos:

class Doctors_Create(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)