from django.apps import AppConfig
from django.db.models import BigAutoField


class GestorConfig(AppConfig):
    name = 'gestor'

default_auto_field = BigAutoField