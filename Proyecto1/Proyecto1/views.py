from django.http import HttpResponse

def saludo(request): #Primera vista
    return HttpResponse("Hola alumnos esta es la nuestra primera pagina de Django")