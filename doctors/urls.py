from django.urls import path

from doctors.views import doctors_index, doctors_create, doctors_create_success, doctors_view, doctors_details, doctors_update, doctors_delete


urlpatterns = [
    path('doctors/', doctors_index, name='doctors_index_path'),
    path('doctors/create/', doctors_create, name='doctors_create_path'),
    path('doctors/create/success/', doctors_create_success, name='doctors_create_success_path'),
    path('doctors/search/', doctors_view, name='doctors_search_path'),
    path('doctors/<int:doctor_id>/delete/', doctors_delete, name='doctors_delete_path'),
    path('doctors/<int:doctor_id>/modify/', doctors_update, name='doctors_modify_path'),
    path('doctors/<int:doctor_id>/details/', doctors_details, name='doctors_details_path')
]