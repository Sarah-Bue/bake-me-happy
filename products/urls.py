from django.urls import path
from . import views

urlpatterns = [
    # All Products
    path('', views.all_products, name='products'),

    # Product Detail Page
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    # Add Product
    path('add/', views.add_product, name='add_product'),

    # Edit Product
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

    # Delete Product
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
]
