from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos', views.ProductListView.as_view(), name='product-list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]

