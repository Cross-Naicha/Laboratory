from django.urls import path

# from main.views import main, patients_create, patients_view, patients_delete, patients_modify, patients_details

from main.views import main, Patients_Create, Patients_View, Patients_Details, Patient_Update, Patients_Delete


urlpatterns = [
    path('', main, name='index_path'),

    # Pacientes
    path('patients/create/', Patients_Create.as_view(), name='patients_create_path'),
    path('patients/search/', Patients_View.as_view(), name='patients_search_path'),
    path('patients/<int:pk>/delete/', Patients_Delete.as_view(), name='patients_delete_path'),
    path('patients/<int:pk>/modify/', Patient_Update.as_view(), name='patients_modify_path'),
    path('patients/<int:pk>/details/', Patients_Details.as_view(), name='patients_details_path')
]
