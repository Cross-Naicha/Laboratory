from django.urls import path
from main.views import main, patients, patients_view

urlpatterns = [
    path('', main, name='index_path'),
    path('resultados/', patients, name='results_path'),
    path('pacientes/', patients_view, name='patients_path')
]
