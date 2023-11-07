from django.shortcuts import render
from django.urls import reverse_lazy

from contacts.models import Suscriptors
# from contacts.forms import Suscriptors_Create

from django.views.generic.edit import CreateView

# def suscriptors(request):
    
#     if request.method == 'POST':
#         suscriptors_form = Suscriptors_Create(request.POST)
#         if suscriptors_form.is_valid():
#             cleaned_suscriptors_form = suscriptors_form.cleaned_data

#             email = cleaned_suscriptors_form.get('email')

#             suscriptors = Suscriptors(email=email)
#             suscriptors.save()

#     suscriptors_form = Suscriptors_Create()
#     return render(request, 'contacts/contacts.html', {'suscriptors_form': suscriptors_form})

class Suscriptors_Create(CreateView):
    model = Suscriptors
    template_name = "contacts/contacts.html"
    fields = ['email']
    success_url = reverse_lazy('contacts_path')
