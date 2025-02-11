from django.urls import path
from . import views

urlpatterns = [
    # All Products
    path('', views.all_products, name='products'),

    # Product Detail
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]