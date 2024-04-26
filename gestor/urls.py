from django.urls import path

from .views import g_consul, g_add, index

urlpatterns = [
    path('', index),
    path('gestor/consul', g_consul),
    path('gestor/add', g_add),
]