from django.contrib import admin

from main.models import *

admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Usuario)
admin.site.register(Colaborador)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(DetallePedido)

# Register your models here.
