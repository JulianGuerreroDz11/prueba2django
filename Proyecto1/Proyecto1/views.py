from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template,Context

def saludo(request): #Primera vista
    #Leer una plantilla de forma manual
    #Abrir ubicacion archivo
    doc_externo=open("C:/Users/pc/Desktop/GitHub/prueba2 django/Proyecto1/Proyecto1/plantillas/miplanquilla.html")
    #Variables
    nombre="Julian"
    apellido="Guerrero"
    fecha_actual=datetime.datetime.now()

    plt=Template(doc_externo.read()) #Creacion objeto template
    doc_externo.close() #Cerramos documento para optimizar recursos
    ctx= Context({"nombre_persona":nombre,"apellido_persona":apellido,"hora_actual":fecha_actual,
    "temas":["Plantillas","Modelos","Formularios","Visitas","Despliegue"]})  #Creacion de contexto (variablos-obj)
    documento=plt.render(ctx)   #Renderizado
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):
    
    return HttpResponse("La hora es %s" %fecha_actual)