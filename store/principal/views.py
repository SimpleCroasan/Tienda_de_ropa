from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse    
from .models import Producto
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
import datetime
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.template import loader
from django.shortcuts import redirect
from .forms import NewUserForm
from .forms import ProductoForm
def main(request):
  
    return render(request, 'index.html')

def informacion(request):
  
    return render(request, 'informacion.html')

def mujer(request):
    producto = Producto.objects.all()
    return render(request, 'mujer.html',{
        'producto' : producto

    })


def hombre(request):
    producto = Producto.objects.all()
    return render(request, 'hombre.html',{
        'producto' : producto

    })

def disenos(request):
    producto = Producto.objects.all()
    return render(request, 'disenos.html',{
        'producto' : producto

    })



def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('main')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html") 
    return HttpResponse(template.render(context,request))


def producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto.html',{'producto':producto})

def lista_producto(request):
    producto = Producto.objects.all()
    return render(request, 'crud.html',{
        'producto' : producto

    })


class UpdateProducto(UpdateView):
    template_name = 'update.html'
    model = Producto
    fields=['Nombre','Descripcion','Precio','Unidades_disponibles','Imagen','categoria']

    def get_success_url(self):
        return reverse_lazy('crud')


class deleteProducto(DeleteView):
    template_name ='borrar.html'
    model= Producto
    
    def get_success_url(self):
        return reverse_lazy('crud')
    

def verProducto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request,'ver.html',{'producto':producto})


def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('crud')  
    else:
        form = ProductoForm()

    return render(request, 'nueva.html', {'form': form})