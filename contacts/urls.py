from django.urls import path

# from contacts.views import suscriptors
from contacts.views import Suscriptors_Create

urlpatterns = [
    path('contacts/', Suscriptors_Create.as_view(), name='contacts_path'),
]
