from django.shortcuts import render


from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from main.models import Producto, Proveedor, Categoria, DetallePedido, Usuario, Cliente, Colaborador, Localizacion, Pedido

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")

class ProductListView(ListView):
    model = Producto

class ProductDetailView(DetailView):
    model = Producto


class LocalizacionListView(ListView):
    model = Localizacion

class LocalizacionDetailView(DetailView):
    model = Localizacion


class DetallePedidoListView(ListView):
    model = DetallePedido

class DetallePedidoDetailView(DetailView):
    model = DetallePedido


class PedidoListView(ListView):
    model = Pedido

class PedidoDetailView(DetailView):
    model = Pedido


class UsuarioListView(ListView):
    model = Usuario

class UsuarioDetailView(DetailView):
    model = Usuario


class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente


class ColaboradorListView(ListView):
    model = Colaborador

class ColaboradorDetailView(DetailView):
    model = Colaborador


class ProveedorListView(ListView):
    model = Proveedor

class ProveedorDetailView(DetailView):
    model = Proveedor


class CategoriaListView(ListView):
    model = Categoria

class CategoriaDetailView(DetailView):
    model = Categoria

