from django.urls import path
from myapp import views

urlpatterns = [
    path('/<nombre>/<int:edad>', views.contenidoHtml),
    path('/sumar/<num1>/<num2>', views.calculadora)
]
