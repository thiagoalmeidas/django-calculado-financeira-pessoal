from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acessar_calculadora(request):
    # Aqui você pode adicionar a lógica para acessar a calculadora
    # Por exemplo, renderizar um template específico
    return render(request, 'teste.html')  # Certifique-se de que o template 'teste.html' existe na pasta de templates

# Create your views here.
def index(request):
    # Aqui você pode adicionar a lógica para acessar a calculadora
    # Por exemplo, renderizar um template específico
    return render(request, 'teste.html')  # Certifique-se de que o template 'teste.html' existe na pasta de templates