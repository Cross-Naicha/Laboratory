from django.urls import path

from accounts.views import login, register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/login/', login, name='accounts_login_path'),
    path('accounts/register/', register, name='accounts_register_path'),
    path('accounts/logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='accounts_logout_path'),
]
