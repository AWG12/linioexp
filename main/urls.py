from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
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

    path('registro/', views.RegistrationView.as_view(), name='register'),

    path('add_to_cart/<int:product_pk>', views.AddToCartView.as_view(), name='add-to-cart'),

    path('remove_from_cart/<int:product_pk>', views.RemoveFromCartView.as_view(), name='remove-from-cart'),

    path('carrito/', views.PedidoDetailView.as_view(), name='pedido-detail'),

    path('checkout/<int:pk>', views.PedidoUpdateView.as_view(), name='pedido-update'),

    path('payment/', views.PaymentView.as_view(), name='payment'),

    path('complete_payment/', views.CompletePaymentView.as_view(), name='complete-payment'),
]
