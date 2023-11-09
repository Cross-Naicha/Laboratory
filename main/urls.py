from django.urls import path

from main.views import main


urlpatterns = [
    path('', main, name='index_path'),
]