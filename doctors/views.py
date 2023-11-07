from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from doctors.models import Doctors
# from doctors.forms import Doctors_Create

from django.views.generic.edit import CreateView


# def doctors(request):
    
#     if request.method == 'POST':
#         doctors_form = Doctors_Create(request.POST)
#         if doctors_form.is_valid():
#             cleaned_doctors_form = doctors_form.cleaned_data

#             name = cleaned_doctors_form.get('name')
#             lastname = cleaned_doctors_form.get('lastname')
#             field = cleaned_doctors_form.get('field')

#             doctors = Doctors(name=name, lastname=lastname, field=field)
#             doctors.save()

#     doctors_form = Doctors_Create()
#     return render(request, 'doctors/doctors.html', {'doctors_form': doctors_form})

class Doctors_Create(CreateView):
    model = Doctors
    template_name = "doctors/doctors.html"
    fields = ['name', 'lastname', 'field']
    success_url = reverse_lazy('doctors_path')

