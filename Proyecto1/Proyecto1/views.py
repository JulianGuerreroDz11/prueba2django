from django.http import HttpResponse
import datetime

def saludo(request): #Primera vista
    return HttpResponse("Hola alumnos esta es la nuestra primera pagina de Django")

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse("La hora es %s" %fecha_actual)