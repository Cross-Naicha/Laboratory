from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from patients.models import Patients
# from main.forms import Patients_Create, Patients_Modify

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

def patients_index(request):
    return render(request, 'patients/patients-index.html', {})

# Patients
# def patients_create(request):

#     if request.method == 'POST':
#         patients_form = Patients_Create(request.POST)
#         if patients_form.is_valid():
#             cleaned_patients_form = patients_form.cleaned_data

#             name = cleaned_patients_form.get('name')
#             lastname = cleaned_patients_form.get('lastname')
#             weight = cleaned_patients_form.get('weight')
#             height = cleaned_patients_form.get('height')
#             bloodGlucose = cleaned_patients_form.get('bloodGlucose')
#             triglycerides = cleaned_patients_form.get('triglycerides')

#             patients = Patients(name=name, lastname=lastname, weight=weight, height=height, bloodGlucose=bloodGlucose, triglycerides=triglycerides)
#             patients.save()

#     patients_form = Patients_Create()   
#     return render(request, 'main/patients-create.html', {'patients_form': patients_form})

class Patients_Create(CreateView):
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

# class Patients_View(ListView):
#     model = Patients
#     context_object_name = 'list_of_patients'
#     template_name = 'main/patients-search.html'


# def patients_delete(request, patient_id):

#     patient_to_delete = Patients.objects.get(id=patient_id)
#     patient_to_delete.delete()

#     return redirect('patients_search_path')

class Patients_Delete(DeleteView):
    model = Patients
    template_name = "patients/patients-delete.html"
    success_url = reverse_lazy('patients_search_path')

# def patients_modify(request, patient_id):

#     patient_to_modify = Patients.objects.get(id=patient_id)

#     if request.method == 'POST':
#         updated_form = Patients_Modify(request.POST)
#         if updated_form.is_valid():
#             updated_form = updated_form.cleaned_data

#             patient_to_modify.name = updated_form.get('name')
#             patient_to_modify.lastname = updated_form.get('lastname')
#             patient_to_modify.weight = updated_form.get('weight')
#             patient_to_modify.height = updated_form.get('height')
#             patient_to_modify.bloodGlucose = updated_form.get('bloodGlucose')
#             patient_to_modify.triglycerides = updated_form.get('triglycerides')           

#             patient_to_modify.save()
#             return redirect('patients_search_path')

#     updated_form = Patients_Modify(initial={'name':patient_to_modify.name, 'lastname':patient_to_modify.lastname, 'weight':patient_to_modify.weight, 'height':patient_to_modify.height, 'bloodGlucose':patient_to_modify.bloodGlucose, 'triglycerides':patient_to_modify.triglycerides})
#     return render(request, 'main/patients-modify.html', {'updated_form':updated_form})

class Patient_Update(UpdateView):
    model = Patients
    template_name = "patients/patients-modify.html"
    fields = ['name', 'lastname', 'weight', 'height', 'bloodGlucose', 'triglycerides']
    success_url = reverse_lazy('patients_search_path')    


# def patients_details(request, patient_id):
    
#     detailed_patient = Patients.objects.get(id=patient_id)
#     return render(request, 'main/patients-details.html', {'detailed_patient':detailed_patient})

class Patients_Details(DetailView):
    model = Patients
    template_name = "patients/patients-details.html"