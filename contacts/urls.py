from django.urls import path
from contacts.views import suscriptors

urlpatterns = [
    path('contacts/', suscriptors, name='contacts_path'),
]
