from django.test import TestCase
from gestor.models import Documento

# Create your tests here.
class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
      cls.x = Documento()
      cls.x.precio = 1
      cls.x.save()

    def test_laboratorio_content(self):
      print("ad")

      print(">>", self.x)

# Create your tests here.
