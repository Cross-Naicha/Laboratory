from django.shortcuts import render, redirect
from main.models import Patients, Doctors, Suscriptors
from main.forms import Patients_Create, Doctors_Create, Suscriptors_Create

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

def patients(request):

    if request.method == 'POST':
        patients_form = Patients_Create(request.POST)
        if patients_form.is_valid():
            cleaned_patients_form = patients_form.cleaned_data

            name = cleaned_patients_form.get('name')
            lastname = cleaned_patients_form.get('lastname')
            weight = cleaned_patients_form.get('weight')
            height = cleaned_patients_form.get('height')
            bloodGlucose = cleaned_patients_form.get('bloodGlucose')
            triglycerides = cleaned_patients_form.get('triglycerides')

            patients = Patients(name=name, lastname=lastname, weight=weight, height=height, bloodGlucose=bloodGlucose, triglycerides=triglycerides)
            patients.save()

    patients_form = Patients_Create()   
    return render(request, 'main/results.html', {'patients_form': patients_form})

def patients_view(request):


    return render(request, 'main/patients.html', {})

def doctors(request):
    
    if request.method == 'POST':
        doctors_form = Doctors_Create(request.POST)
        if doctors_form.is_valid():
            cleaned_doctors_form = doctors_form.cleaned_data

            name = cleaned_doctors_form.get('name')
            lastname = cleaned_doctors_form.get('lastname')
            field = cleaned_doctors_form.get('field')

            doctors = Doctors(name=name, lastname=lastname, field=field)
            doctors.save()

    doctors_form = Doctors_Create()
    return render(request, 'main/doctors.html', {'doctors_form': doctors_form})

def suscriptors(request):
    
    if request.method == 'POST':
        suscriptors_form = Suscriptors_Create(request.POST)
        if suscriptors_form.is_valid():
            cleaned_suscriptors_form = suscriptors_form.cleaned_data

            email = cleaned_suscriptors_form.get('email')

            suscriptors = Suscriptors(email=email)
            suscriptors.save()

    suscriptors_form = Suscriptors_Create()
    return render(request, 'main/contacts.html', {'suscriptors_form': suscriptors_form})