from django.shortcuts import render
from main.models import Patients

# Create your views here:
def main(request):
    return render(request, 'main/index.html', {})

def patients(request):
    
    print(request.POST)

    if request.method == 'POST':

        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        bloodGlucose = request.POST.get('bloodGlucose')
        triglycerides = request.POST.get('triglycerides')

        patient = Patients(name=name, lastname=lastname, height=height, weight=weight, bloodGlucose=bloodGlucose, triglycerides=triglycerides)
        patient.save()

    return render(request, 'main/results.html', {})
