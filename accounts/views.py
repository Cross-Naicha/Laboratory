from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login

from accounts.forms import User_Registration

def login(request):
    
    authentication_form = AuthenticationForm()

    if request.method == 'POST':
        authentication_form = AuthenticationForm(request, data=request.POST)
        if authentication_form.is_valid():
            user = authentication_form.cleaned_data.get('username')
            password = authentication_form.cleaned_data.get('password')

            active_user = authenticate(username=user, password=password)

            auth_login(request, active_user)

            return redirect('index_path')
        else:
            return render(request, 'accounts/login-denied.html', {})

    return render(request, 'accounts/login.html', {'authentication_form': authentication_form})

def register(request):
    registration_form = User_Registration()

    if request.method == 'POST':
        registration_form = User_Registration(request.POST)
        if registration_form.is_valid():

            registration_form.save()
            return redirect('accounts_login_path')

    return render(request, 'accounts/register.html', {'registration_form':registration_form})
