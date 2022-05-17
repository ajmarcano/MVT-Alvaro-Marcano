from django.http import HttpResponse
from django.shortcuts import render
from .models import familiaLopez

def listadoFamiliar(request):
    familiares = familiaLopez.objects.all()
   
    context = {'familiares': familiares}

    return render(request, 'template.html', context)