from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentoForm
from .models import Documento


def consultar_documentos(request):
    if request.method == 'POST' and 'eliminar' in request.POST:
        documento_id = request.POST.get('documento_id')
        documento = get_object_or_404(Documento, id=documento_id)
        documento.delete()
        messages.success(request, "Documento eliminado correctamente.")
        return redirect('consultar_documentos')
    documentos = Documento.objects.all()
    
    return render(
      request, 
      'documentos/consultar_documentos.html', 
      {'documentos': documentos}
  )


def agregar_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Documento agregado correctamente.")
            return redirect('consultar_documentos')
        else:
            messages.error(request, "Hubo un error al agregar el documento.")
    else:
        form = DocumentoForm()
    return render(request, 'documentos/agregar_documento.html', {'form': form})







# Create your views here.
