from django.shortcuts import render
from main.models import Patients

# Create your views here:
def main(request):
    return render(request, 'main.html', {})

def patients(request):
    
    patient = Patients(name='Blue', lastname='Label', height=1.8, weight=80, bloodGlucose=90, triglycerides=120)
    patient.save()

    return render(request, 'results.html', {'patients': patient})