from django.urls import path

# from main.views import patients_create, patients_view, patients_delete, patients_modify, patients_details
from patients.views import patients_index, Patients_Create, patients_create_success, patients_view, Patients_Details, Patient_Update, Patients_Delete


urlpatterns = [
    path('patients/', patients_index, name='patients_index_path'),
    path('patients/create/', Patients_Create.as_view(), name='patients_create_path'),
    path('patients/create/success', patients_create_success, name='patients_create_success_path'),
    path('patients/search/', patients_view, name='patients_search_path'),
    path('patients/<int:pk>/delete/', Patients_Delete.as_view(), name='patients_delete_path'),
    path('patients/<int:pk>/modify/', Patient_Update.as_view(), name='patients_modify_path'),
    path('patients/<int:pk>/details/', Patients_Details.as_view(), name='patients_details_path')
]