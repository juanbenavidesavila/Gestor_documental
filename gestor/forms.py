from django import forms
from django.contrib.auth.models import User

from .models import Documento


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
                  'titulo', 
                  'folio', 
                  'archivo']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return User