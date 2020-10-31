from django.contrib import admin

from main.models import *

admin.site.register(Localizacion)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(DetallePedido)


class ClienteInline(admin.TabularInline):
    model = Cliente


class ColaboradorInline(admin.TabularInline):
    model = Colaborador


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]


admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Profile, ProfileAdmin)

class ProductoImageInline(admin.TabularInline):
    model=ProductoImage


class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ProductoImageInline,
    ]

admin.site.register(Producto, ProductoAdmin)
