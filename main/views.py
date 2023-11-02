from django.shortcuts import render, redirect
from main.models import Patients, Doctors, Suscriptors
# from main.forms import Patient

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

def patients(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        bloodGlucose = request.POST.get('bloodGlucose')
        triglycerides = request.POST.get('triglycerides')

        patient = Patients(name=name, lastname=lastname, height=height, weight=weight, bloodGlucose=bloodGlucose, triglycerides=triglycerides)
        patient.save()

        return redirect('patients_path')

    return render(request, 'main/results.html', {})

def patients_view(request):

    search_id = request.GET.get('lastname')

    if search_id:
        patients_list = Patients.objects.filter(lastname=search_id) 
    else:
        patients_list = Patients.objects.all()

    return render(request, 'main/patients.html', {'patients_list': patients_list})

def doctors(request):
    
    if request.method == 'POST':

        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        field = request.POST.get('field')

        doctor = Doctors(name=name, lastname=lastname, field=field)
        doctor.save()

        return redirect('index_path')

    return render(request, 'main/doctors.html', {})

def suscriptors(request):
    
    if request.method == 'POST':

        email = request.POST.get('email')

        suscriptor = Suscriptors(email=email)
        suscriptor.save()

        return redirect('index_path')

    return render(request, 'main/contact.html', {})