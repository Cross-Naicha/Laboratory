from django.urls import path
from main.views import main, patients, patients_view, doctors, suscriptors

urlpatterns = [
    path('', main, name='index_path'),
    path('resultados/', patients, name='results_path'),
    path('pacientes/', patients_view, name='patients_path'),
    path('medicos/', doctors, name='doctors_path'),
    path('contacto/', suscriptors, name='contact_path'),
]
