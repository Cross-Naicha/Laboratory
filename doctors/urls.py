from django.urls import path

# from doctors.views import doctors

from doctors.views import Doctors_View

urlpatterns = [
    path('doctors/', Doctors_View.as_view(), name='doctors_path'),
]