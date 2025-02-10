from django.urls import path
from . import views

urlpatterns = [
    # Product Overview
    path('', views.all_products, name='products'),
]