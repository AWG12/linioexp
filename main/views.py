from django.shortcuts import render


from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from main.models import Producto

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")

class ProductListView(ListView):
    model = Producto

class ProductDetailView(DetailView):
    model = Producto
