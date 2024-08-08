from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Producto, Proveedor
from .forms import ClienteForm, ProductoForm, ProveedorForm

def index(request):
    return render(request, 'app/index.html')

def clientes(request): 
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el cliente en la base de datos
            return redirect('index')  # Redirige a la página principal
    else:
        form = ClienteForm()
    return render(request, 'app/clientes.html', {'form': form})

def productos(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('index')  # Redirige a la página principal
    else:
        form = ClienteForm()
    return render(request, 'app/productos.html', {'form': form})

def proveedores(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el proveedor en la base de datos
            return redirect('index')  # Redirige a la página principal
    else:
        form = ClienteForm()
    return render(request, 'app/proveedores.html', {'form': form})


def search(request):
    query = request.GET.get('query', '')

    cliente = Cliente.objects.filter(nombre__icontains=query)
    producto = Producto.objects.filter(nombre__icontains=query)
    proveedore = Proveedor.objects.filter(nombre__icontains=query)

    context = {
        'clientes': cliente,
        'productos': producto,
        'proveedores': proveedore,
    }

    return render(request, 'app/search.html', context)

def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('search')

def delete_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('search')

def delete_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect('search')
