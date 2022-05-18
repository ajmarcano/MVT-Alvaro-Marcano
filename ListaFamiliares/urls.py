from django.urls import path
from . import views

urlpatterns = [
    path('', views.listadoFamiliar, name="listadoFamiliar"),
]