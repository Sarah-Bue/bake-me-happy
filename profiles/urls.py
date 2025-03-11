from django.urls import path
from . import views

urlpatterns = [
    # Profile
    path('', views.profile, name='profile'),

    # Orders
    path('orders/', views.orders, name='orders'),

    # Order History
    path('order_history/<order_number>', views.order_history, name='order_history'),

    # Delete Profile
    path('delete_profile/', views.delete_profile, name='delete_profile'),
]