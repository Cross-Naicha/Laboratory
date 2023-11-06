from django.urls import path
from main.views import main, patients_create, patients_view, patients_delete, patients_modify, patients_details

urlpatterns = [
    path('', main, name='index_path'),

    # Pacientes
    path('patients/create/', patients_create, name='patients_create_path'),
    path('patients/search/', patients_view, name='patients_search_path'),
    path('patients/<int:patient_id>/delete/', patients_delete, name='patients_delete_path'),
    path('patients/<int:patient_id>/modify/', patients_modify, name='patients_modify_path'),
    path('patients/<int:patient_id>/details/', patients_details, name='patients_details_path')
]
