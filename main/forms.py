from django import forms

# Create your forms here:

# Pacientes:
class Patients(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    weight = forms.CharField(max_length=10)
    height = forms.FloatField()
    bloodGlucose = forms.FloatField()
    triglycerides = forms.FloatField()

class Patients_Create(Patients):
    ...

# Medicos:

class Doctors(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)

class Doctors_Create(Doctors):
    ...

# Suscriptores:

class Suscriptors(forms.Form):
    email = forms.CharField(max_length=30)

class Suscriptors_Create(Suscriptors):
    ...