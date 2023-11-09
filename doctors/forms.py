from django import forms


class Doctors_Blueprint(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)
class Doctors_Create(Doctors_Blueprint):
    ...

class Doctors_Update(Doctors_Blueprint):
    ...