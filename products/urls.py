from django.urls import path
from . import views

urlpatterns = [
    # All Products
    path('', views.all_products, name='products'),

    # Product Detail Page
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    # Add Product
    path('add/', views.add_product, name='add_product'),
]