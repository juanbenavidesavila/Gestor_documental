from django.urls import path

from . import views

urlpatterns = [
    path('', views.consultar_documentos, name='consultar_documentos'),
    path('agregar/', views.agregar_documento, name='agregar_documento'),
]