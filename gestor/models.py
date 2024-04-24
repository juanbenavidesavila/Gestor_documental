from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

class Departamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

class SubDepartamento(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

class Documento(models.Model):
    sub_departamento = models.ForeignKey(SubDepartamento, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    folio = models.CharField(max_length=50)
    archivo = models.FileField(upload_to='documentos/')

    def _str_(self):
        return self.titulo
