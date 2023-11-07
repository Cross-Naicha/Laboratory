from django.urls import path

from main.views import main, login


urlpatterns = [
    path('', login, name='accounts_path'),
    path('index/', main, name='index_path'),
]
