from django.urls import path
from main.views import main, patients

urlpatterns = [
    path('', main),
    path('resultados/', patients)
]
