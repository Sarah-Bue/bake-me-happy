from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    # Checkout
    path('', views.checkout, name='checkout'),

    # Checkout Success
    path(
        'checkout_success/<order_number>',
        views.checkout_success,
        name='checkout_success'
    ),

    # Webhooks
    path('wh/', webhook, name='webhook'),

    # Cache Checkout Data
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
]
