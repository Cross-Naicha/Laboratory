from django.shortcuts import render, redirect
from main.models import Patients, Doctors, Suscriptors
from main.forms import Patients_Create, Patients_Modify, Doctors_Create, Suscriptors_Create

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

# Patients
def patients_create(request):

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
    return render(request, 'main/patients-create.html', {'patients_form': patients_form})

def patients_view(request):

    search_target = request.GET.get('lastname')

    if search_target:
        list_of_patients = Patients.objects.filter(lastname__icontains=search_target)
    else:
        list_of_patients = Patients.objects.all()

    return render(request, 'main/patients-search.html', {'list_of_patients': list_of_patients})

def patients_delete(request, patient_id):

    patient_to_delete = Patients.objects.get(id=patient_id)
    patient_to_delete.delete()

    return redirect('patients_path')

def patients_modify(request, patient_id):

    patient_to_modify = Patients.objects.get(id=patient_id)

    if request.method == 'POST':
        updated_form = Patients_Modify(request.POST)
        if updated_form.is_valid():
            updated_form = updated_form.cleaned_data

            patient_to_modify.name = updated_form.get('name')
            patient_to_modify.lastname = updated_form.get('lastname')
            patient_to_modify.weight = updated_form.get('weight')
            patient_to_modify.height = updated_form.get('height')
            patient_to_modify.bloodGlucose = updated_form.get('bloodGlucose')
            patient_to_modify.triglycerides = updated_form.get('triglycerides')           

            patient_to_modify.save()
            return redirect('patients_path')

    updated_form = Patients_Modify(initial={'name':patient_to_modify.name, 'lastname':patient_to_modify.lastname, 'weight':patient_to_modify.weight, 'height':patient_to_modify.height, 'bloodGlucose':patient_to_modify.bloodGlucose, 'triglycerides':patient_to_modify.triglycerides})
    return render(request, 'main/patients-modify.html', {'updated_form':updated_form})

def patients_details(request, patient_id):
    
    detailed_patient = Patients.objects.get(id=patient_id)
    return render(request, 'main/patients-details.html', {'detailed_patient':detailed_patient})

# Doctors
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

# Suscriptors
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