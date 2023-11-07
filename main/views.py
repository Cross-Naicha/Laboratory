from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

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
            return render(request, 'main/login-denied.html', {})

    return render(request, 'main/login.html', {'authentication_form': authentication_form})

def register(request):
    return render(request, 'main/register.html', {})
    

