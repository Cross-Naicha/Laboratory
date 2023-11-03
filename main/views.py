from django.shortcuts import render, redirect
from main.forms import Patients_Create, Doctors_Create, Suscriptors_Create

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

def patients(request):

    if request.method == 'POST':
        ...

    patients_form = Patients_Create()
    return render(request, 'main/results.html', {'patients_form': patients_form})

def patients_view(request):


    return render(request, 'main/patients.html', {})

def doctors(request):
    
    if request.method == 'POST':
        ...

    doctors_form = Doctors_Create()
    return render(request, 'main/doctors.html', {'doctors_form': doctors_form})

def suscriptors(request):
    
    if request.method == 'POST':
        ...

    suscriptors_form = Suscriptors_Create()
    return render(request, 'main/contacts.html', {'suscriptors_form': suscriptors_form})