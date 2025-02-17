from django.urls import path
from . import views

urlpatterns = [
    # Checkout
    path('', views.checkout, name='checkout'),

    # Checkout Success
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]