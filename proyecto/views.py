from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    saludo = "Hola"
    pag = HttpResponse(saludo)
    return pag

