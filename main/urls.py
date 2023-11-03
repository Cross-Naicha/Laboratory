from django.urls import path
from main.views import main, patients, patients_view, doctors, suscriptors

urlpatterns = [
    path('', main, name='index_path'),
    path('results/', patients, name='results_path'),
    path('patients/', patients_view, name='patients_path'),
    path('doctors/', doctors, name='doctors_path'),
    path('contacts/', suscriptors, name='contacts_path'),
]
