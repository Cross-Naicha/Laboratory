from django.shortcuts import render

from contacts.models import Suscriptors
from contacts.forms import Suscriptors_Create

def suscriptors(request):
    
    if request.method == 'POST':
        suscriptors_form = Suscriptors_Create(request.POST)
        if suscriptors_form.is_valid():
            cleaned_suscriptors_form = suscriptors_form.cleaned_data

            email = cleaned_suscriptors_form.get('email')

            suscriptors = Suscriptors(email=email)
            suscriptors.save()

    suscriptors_form = Suscriptors_Create()
    return render(request, 'contacts/contacts.html', {'suscriptors_form': suscriptors_form})
