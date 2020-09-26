from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos', views.ProductListView.as_view(), name='product-list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('proveedores', views.ProveedorListView.as_view(), name='proveedor-list'),
    path('proveedores/<int:pk>', views.ProveedorDetailView.as_view(), name='proveedor-detail'),

    path('categorias', views.CategoriaListView.as_view(), name='categorias-list'),
    path('categorias/<int:pk>', views.CategoriaDetailView.as_view(), name='categorias-detail'),

    path('localizaciones', views.LocalizacionListView.as_view(), name='localizaciones-list'),
    path('localizaciones/<int:pk>', views.LocalizacionDetailView.as_view(), name='localizaciones-detail'),

    path('detallepedido', views.DetallePedidoListView.as_view(), name='detallepedido-list'),
    path('detallepedido/<int:pk>', views.DetallePedidoDetailView.as_view(), name='detallepedido-detail'),

    path('pedidos', views.PedidoListView.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>', views.PedidoDetailView.as_view(), name='pedido-detail'),

    path('usuarios', views.UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>', views.UsuarioDetailView.as_view(), name='usuario-detail'),

    path('clientes', views.ClienteListView.as_view(), name='clientes-list'),
    path('clientes/<int:pk>', views.ClienteDetailView.as_view(), name='clientes-detail'),

    path('colaboradores', views.ColaboradorListView.as_view(), name='colaborador-list'),
    path('colaboradores/<int:pk>', views.ColaboradorDetailView.as_view(), name='colaborador-detail'),
]

