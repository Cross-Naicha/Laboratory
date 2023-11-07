from django.urls import path

from main.views import main, login, register
from main.forms import User_Registration
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', login, name='accounts_login_path'),
    path('accounts/register/', register, name='accounts_register_path'),
    path('accounts/logout/', LogoutView.as_view(template_name='main/logout.html'), name='accounts_logout_path'),
    path('index/', main, name='index_path'),
]
