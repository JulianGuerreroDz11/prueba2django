from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template,Context, loader
from django.shortcuts import render


#Variables
nombre="Julian"
apellido="Guerrero" 
fecha_actual=datetime.datetime.now()

def saludo(request): #Primera vista
    """ #FORMA MANUAL
    #Leer una plantilla de forma manual
    #Abrir ubicacion archivo
    doc_externo=open("C:/Users/pc/Desktop/GitHub/prueba2 django/Proyecto1/Proyecto1/plantillas/miplanquilla.html")    
    plt=Template(doc_externo.read()) #Creacion objeto template
    doc_externo.close() #Cerramos documento para optimizar recursos
    ctx= Context({"nombre_persona":nombre,"apellido_persona":apellido,"hora_actual":fecha_actual,
    "temas":["Plantillas","Modelos","Formularios","Visitas","Despliegue"]})  #Creacion de contexto (variablos-obj)
    documento=plt.render(ctx)   #Renderizado
    return HttpResponse(documento)
    """
    """
    #FORMA USANDO LOADER NO OLVIDAR LA DIRECCION AGREGADA EN SETTINGS
    doc_externo=loader.get_template('miplanquilla.html')  
    documento=doc_externo.render({"nombre_persona":nombre,"apellido_persona":apellido,"hora_actual":fecha_actual,
    "temas":["Plantillas","Modelos","Formularios","Visitas","Despliegue"]})
    return HttpResponse(documento)
    """
    #FORMA USANDO RENDER NO OLVIDAR LA DIRECION AGREGADA EN SETTINGS
    return render(request,"miplanquilla.html",{"nombre_persona":nombre,"apellido_persona":apellido,"hora_actual":fecha_actual,
    "temas":["Plantillas","Modelos","Formularios","Visitas","Despliegue"]})

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):    
    return HttpResponse("La hora es %s" %fecha_actual)