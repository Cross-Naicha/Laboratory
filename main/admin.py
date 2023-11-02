from django.contrib import admin
from main.models import Patients, Doctors, Suscriptors

# Register your models here.
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Suscriptors)