from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acesso_calculadora/', views.acessar_calculadora)
]