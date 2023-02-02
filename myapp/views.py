from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP
def contenidoHtml(req, nombre, edad):
    contenido = """
        <html>
            <body>
                <p>Nombre: %s / Edad: %s </p>
            </body>
        </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)

def calculadora(request, num1, num2):
    op1 = int(num1)
    op2 = int(num2)
    context = { 'result': op1 + op2 }
    response = render(request, 'suma.html', context)
    return response
