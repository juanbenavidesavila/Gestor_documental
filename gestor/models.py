from django.db import models


class Documento(models.Model):
  tipo_documentos = [
                    ["General", "General"],
                    ["Circular", "Circular"],
                    ["Minuta", "Minuta"],
                    ["Nota", "Nota"],
                    ["Oficio", "Oficio"],
                   ]
  documento = models.CharField(max_length=20, 
                                choices=tipo_documentos, 
                                default="General")
  
  departamentos = [
                  ["Contabilidad", "Contabilidad"],
                  ["Administracion", "Administracion"],
                  ["Secreataria", "Secretaria"],
                  ["RRHH", "RRHH"],
                  ["Informatica", "Informatica"],
                  ["Finanzas", "Finanzas"],
                  ["Sistemas", "Sistemas"],
                  ["Educacion", "Educacion"],
                  ]  
  
  departamento = models.CharField(max_length=20, 
                                  choices=departamentos, 
                                  default="Informatica")

  titulo = models.CharField(max_length=50)

  folio = models.CharField(max_length=20)
  
  año = models.CharField(max_length=5, default="2024")

  mes = models.CharField(max_length=5, default="01")
  
  archivo = models.FileField(upload_to='documentos/')
  
  #auto_now_add Se anade una sola vez, cuando se crea el registro
  creacion = models.DateTimeField(auto_now_add=True)
  #auto_now Se modifica con cada cambio que se realize en el registro
  modificacion = models.DateTimeField(auto_now=True)

  class Meta:
      permissions = [("consultar_documentos", "Consultar documentos")]

      permissions = [("agregar_documento", "Agregar documento")]
    
      permissions = [("eliminar_documento", "Eliminar documento")]