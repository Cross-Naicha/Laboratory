from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import PasswordChangeView 

from accounts.forms import User_Registration, User_Edition
from accounts.models import OtherUserData


def login(request):
    
    authentication_form = AuthenticationForm()

    if request.method == 'POST':
        authentication_form = AuthenticationForm(request, data=request.POST)
        if authentication_form.is_valid():
            user = authentication_form.cleaned_data.get('username')
            password = authentication_form.cleaned_data.get('password')

            active_user = authenticate(username=user, password=password)

            auth_login(request, active_user)

            OtherUserData.objects.get_or_create(user=request.user)

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

def profile_view(request):

    users_form = request.user
    return render(request, 'accounts/profile-view.html', {'users_form':users_form})

def profile_edit_user(request):

    otheruserdata = request.user.otheruserdata
    edition_form = User_Edition(initial= {'institution': otheruserdata.institution, 'institutional_mail': otheruserdata.institutional_mail}, instance=request.user)

    if request.method == 'POST':
        edition_form = User_Edition(request.POST, instance=request.user)
        if edition_form.is_valid():
            
            institution = edition_form.cleaned_data.get('institution')
            institutional_mail = edition_form.cleaned_data.get('institutional_mail')

            if institution:
                otheruserdata.institution = institution
                otheruserdata.save()

            if institutional_mail:
                otheruserdata.institutional_mail = institutional_mail
                otheruserdata.save()
            
            edition_form.save()

            return redirect('accounts_view_path')

    return render(request, 'accounts/profile-edit.html', {'edition_form':edition_form})

class Profile_Change_Password(PasswordChangeView):
    template_name = 'accounts/profile-edit-password.html'
    success_url = reverse_lazy('index_path')