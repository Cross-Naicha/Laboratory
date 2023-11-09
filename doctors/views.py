from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from doctors.models import Doctors
from doctors.forms import Doctors_Create, Doctors_Update

def doctors_index(request):
    return render(request, 'doctors/doctors-index.html', {})

def doctors_create(request):
    

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
    return render(request, 'doctors/doctors-create.html', {'doctors_form': doctors_form})


def doctors_view(request):

    search_target = request.GET.get('field')

    if search_target:
        list_of_doctors = Doctors.objects.filter(field__icontains=search_target)
    else:
        list_of_doctors = Doctors.objects.all()

    return render(request, 'doctors/doctors-search.html', {'list_of_doctors': list_of_doctors})


def doctors_delete(request, doctor_id):

    doctor_to_delete = Doctors.objects.get(id=doctor_id)
    doctor_to_delete.delete()

    return redirect('doctors_search_path')


def doctors_update(request, doctor_id):

    doctor_to_modify = Doctors.objects.get(id=doctor_id)

    if request.method == 'POST':
        updated_form = Doctors_Update(request.POST)
        if updated_form.is_valid():
            updated_form = updated_form.cleaned_data

            doctor_to_modify.name = updated_form.get('name')
            doctor_to_modify.lastname = updated_form.get('lastname')
            doctor_to_modify.field = updated_form.get('field')

            doctor_to_modify.save()
            return redirect('doctors_search_path')

    updated_form = Doctors_Update(initial={'name':doctor_to_modify.name, 'lastname':doctor_to_modify.lastname, 'field':doctor_to_modify.field})
    return render(request, 'doctors/doctors-modify.html', {'updated_form':updated_form})


def doctors_details(request, doctor_id):
    
    detailed_doctor = Doctors.objects.get(id=doctor_id)
    return render(request, 'doctors/doctors-details.html', {'detailed_doctor':detailed_doctor})
