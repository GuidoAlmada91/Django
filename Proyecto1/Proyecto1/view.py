from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola Django - Coder House")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es día: <br> {dia}"
    return HttpResponse(texto)

def probando_template(request):
    
    
    nombre = "Guido"
    apellido = "Almada"
    lista_de_notas=[1,2,3,4,5,6,7,8,9,10]

    
    mi_html = open("C:/Users/Loyolla/Desktop/proyecto_django/Proyecto1/Proyecto1/templates/template1.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    
    diccionario=Context({"nombre": nombre, "apellido": apellido, "hoy": datetime.datetime.now, "notas": lista_de_notas})


    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

