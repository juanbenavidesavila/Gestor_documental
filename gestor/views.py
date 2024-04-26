from django.shortcuts import render
from .forms import DocumentoForm
from .models import Documento


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

#from django.contrib.auth.decorators import login_required, permission_required

#@login_required(login_url="/admin/login/")
#@permission_required('gestor.consultar_documentos',
 #                    login_url="/admin/login/")


def g_consul(request):
  datos = Documento.objects.all()
  if request.GET.get('folio', None) != None: #cuando sea diferente
    datos = datos.filter(folio__icontains = request.GET.get('folio'))

  if request.GET.get('titulo', None) != None: #cuando sea diferente
    datos = datos.filter(titulo__icontains = request.GET.get('titulo'))

  context = {'doc': datos}
  return render(request, "consultar_documentos.html", context)


#@login_required(login_url="/admin/login/")
#@permission_required('gestor.agregar_documento', login_url="/admin/login/")

def g_add(request):
    if request.method == 'POST':  # Si la peticion proviene de un metodo POST
        data = DocumentoForm(
            request.POST)  # Datos del metodo post inserto en el form
        if data.is_valid():  # Los datos cruzan las validaciones
            data.save()  # Guarda en base de datos

    # Se muestra cuando la peticion no sea POST
    # Se muestra cuando la peticion POST ha terminado
    context = {"form": DocumentoForm()}
    return render(request, "agregar_documentos.html", context)

  


#def consultar_documentos(request):
  #  if request.method == 'POST' and 'eliminar' in request.POST:
   #     documento_id = request.POST.get('documento_id')
    #    documento = get_object_or_404(Documento, id=documento_id)
     #   documento.delete()
      #  messages.success(request, "Documento eliminado correctamente.")
      #  return redirect('consultar_documentos')
    #documentos = Documento.objects.all()
    
    #return render(
     # request, 
      #'documentos/consultar_documentos.html', 
     # {'documentos': documentos}
  #)

#def agregar_documento(request):
 #   if request.method == 'POST':
  #      form = DocumentoForm(request.POST, request.FILES)
   #     if form.is_valid():
    #        form.save()
     #       messages.success(request, "Documento agregado correctamente.")
      #      return redirect('consultar_documentos')
       # else:
        #    messages.error(request, "Hubo un error al agregar el documento.")
    #else:
   #     form = DocumentoForm()
    #return render(request, 'documentos/agregar_documento.html', {'form': form})







# Create your views here.
