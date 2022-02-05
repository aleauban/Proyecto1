from django.http import HttpResponse
from datetime import date #importa fecha
from datetime import datetime #importa fecha + hora
import locale
locale.setlocale(locale.LC_ALL, 'es_ES')    #convertir fechas en formato español


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<h1>Hola!</h1></br><p>Recuerden que esta es mi segunda vista</p>")  
    #esto es en codigo HTML
    #<h1> que es un Titulo grande, </br> salto de linea, <p> que es un parrafo 

def dia_de_hoy(request):
    hoy = datetime.now()
    message = f"<h1>Hola!</h1></br><p>Recuerden que hoy es {hoy}</p>"
    return HttpResponse(message)

def dia_de_hoy1(request):
    hoy = date.today() 
    message = f"<h1>Hola!</h1></br><p>Recuerden que hoy es {hoy.day}-{hoy.month}-{hoy.year}</p>"
    return HttpResponse(message)

def dia_de_hoy2(request):
    hoy = date.today() 
    # https://aprendeconalf.es/docencia/python/manual/datetime/
    message = f"<h1>Hola!</h1></br><p>Recuerden que hoy es {hoy.strftime('%d-%m-%y')}, {hoy.strftime('%A-%B-%Y')}, {hoy.strftime('%a.%B.%Y')}</p>"
    return HttpResponse(message)

def mi_nombre(request, nombre):
    message = f"<h1>Hola!</h1></br><p>Recuerden que la persona conectada es {nombre}</p>"
    return HttpResponse(message)

def anio_nacimiento(request, edad):
    hoy = date.today()
    anios = int(edad)
    resultado = hoy.year - anios
    message = f"<h1>Hola!</h1></br><p>Tu naciciste en el año {resultado}</p>"
    return HttpResponse(message)