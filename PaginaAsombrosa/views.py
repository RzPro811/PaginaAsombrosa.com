from django.template import Template, Context
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    saludo = "Bienvenido a Pagina Asombrosa .com"
    return HttpResponse(saludo)

def bienvenida(request, nombre, apellido):
    saludo = f"Bienvenido {nombre} {apellido} a PaginaAsombrosa.com"
    return HttpResponse(saludo)

def bienvenida_html(request, nombre, apellido):
    saludo= f"""
<Head>
<html>
<h1>Bienvenido a PAGINA ASOMBROSA .COM!!!</h1>
<h2>como estas señor o señora {nombre} {apellido}?!</h2>
</html>
</head>"""
    return saludo

def bienvenida_tmpl(request):
    with open("C:/Users/joelz/OneDrive/Imágenes/Documentos/DjangoClases/carpeta/pagina_asombrosa.com/PaginaAsombrosa/PaginaAsombrosa/plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)
    return HttpResponse(saludo)