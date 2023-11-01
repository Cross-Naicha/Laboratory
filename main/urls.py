from django.urls import path
from main.views import main, patients

urlpatterns = [
    path('', main, name='index_path'),
    path('resultados/', patients, name='resultados_path')
]
