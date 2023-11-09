from django.urls import path

from accounts.views import login, register, profile_view, profile_edit_user, Profile_Change_Password
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/login/', login, name='accounts_login_path'),
    path('accounts/register/', register, name='accounts_register_path'),
    path('accounts/logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='accounts_logout_path'),
    path('accounts/profile-view/', profile_view, name='accounts_view_path'),
    path('accounts/profile-edit/', profile_edit_user, name='accounts_edit_path'),
    path('accounts/profile-edit/password/', Profile_Change_Password.as_view(), name='accounts_edit_password_path'),
]
