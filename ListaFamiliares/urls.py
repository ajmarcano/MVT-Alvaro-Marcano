from ListaFamiliares.views import listadoFamiliar
from django.urls import path

urlpatterns = [
    path('familiares/', listadoFamiliar),
]