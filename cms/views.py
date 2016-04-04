from django.shortcuts import render
from django.http import HttpResponse

from models import Pages

# Create your views here.

def nuevorecurso(request, uno, dos):
    recurso = Pages(Name=uno, Page=dos)
    recurso.save()
    return HttpResponse("Todo ha ido bien")

def recurso(request, identificador):
    try:
        recurso = Pages.objects.get(id=identificador)
        print(recurso.Page)
        respuesta ='<ol><li><a href="http://'+str(recurso.Page)+'">'+recurso.Name+'</a></ol>'
    except Pages.DoesNotExist:
        respuesta = "El recurso solicitado no existe"
    return HttpResponse(respuesta)

def index(request):
    lista_recursos = Pages.objects.all()
    respuesta = "<ol>"
    for recurso in lista_recursos:
        respuesta += '<li><a href='+str(recurso.Page)+'>'+recurso.Name+'</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)

def el404(request):
    return HttpResponse("La pagina solicitada no existe")
