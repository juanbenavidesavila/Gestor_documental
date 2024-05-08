from django import forms
from .models import Documento


class DocumentoForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(DocumentoForm, self).__init__(*args, **kwargs)
      self.fields['titulo'].widget.attrs['class'] = 'form-control'
      self.fields['folio'].widget.attrs['class'] = 'form-control'

  class Meta:
      model = Documento
      exclude = []