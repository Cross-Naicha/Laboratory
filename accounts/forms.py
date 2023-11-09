from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class User_Registration(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

class User_Edition(UserChangeForm):

    password = None
    email = forms.EmailField(label= 'E-Mail', required=False)
    first_name = forms.CharField(label= 'Nombre', required=False)
    last_name = forms.CharField(label= 'Apellido', required=False)
    institution = forms.CharField(max_length=100, required=False)
    institutional_mail = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']