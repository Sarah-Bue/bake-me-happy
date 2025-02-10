from django.urls import path
from . import views

urlpatterns = [
    # Product Overview
    path('', views.product_list, name='products'),
]