from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder House")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es día: <br> {dia}"
    return HttpResponse(texto)

def probando_template(request):
    nombre = "Guido"
    apellido = "Almada"

    diccionario = {"Nombre:": nombre, "Apellido: ": apellido}
    mi_html = open("Proyecto1/templates/template1.html", "r")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(diccionario)
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)