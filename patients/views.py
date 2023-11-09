from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from patients.models import Patients

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def patients_index(request):
    return render(request, 'patients/patients-index.html', {})

class Patients_Create(LoginRequiredMixin, CreateView):
    model = Patients
    template_name = "patients/patients-create.html"
    fields = ['name', 'lastname', 'weight', 'height', 'bloodGlucose', 'triglycerides']
    success_url = reverse_lazy('patients_create_path')

def patients_view(request):

    search_target = request.GET.get('lastname')

    if search_target:
        list_of_patients = Patients.objects.filter(lastname__icontains=search_target)
    else:
        list_of_patients = Patients.objects.all()

    return render(request, 'patients/patients-search.html', {'list_of_patients': list_of_patients})


class Patients_Delete(LoginRequiredMixin, DeleteView):
    model = Patients
    template_name = "patients/patients-delete.html"
    success_url = reverse_lazy('patients_search_path')


class Patient_Update(LoginRequiredMixin, UpdateView):
    model = Patients
    template_name = "patients/patients-modify.html"
    fields = ['name', 'lastname', 'weight', 'height', 'bloodGlucose', 'triglycerides']
    success_url = reverse_lazy('patients_search_path')    


class Patients_Details(DetailView):
    model = Patients
    template_name = "patients/patients-details.html"