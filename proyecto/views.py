from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    saludo = "Hola"
    pag = HttpResponse(saludo)
    return pag

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="control_estudios/base.html",
        context=contexto,
    )
    return http_response