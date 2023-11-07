from django.urls import path

# from doctors.views import doctors

from doctors.views import Doctors_Create

urlpatterns = [
    path('doctors/', Doctors_Create.as_view(), name='doctors_path'),
]