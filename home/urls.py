from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='home'),

    # Store Management Page
    path('store_management/', views.store_management, name='store_management'),

    # Manage Orders
    path('manage-orders/', views.manage_orders, name='manage_orders'),

    # Manage Subscribers
    path('manage-subscribers/', views.manage_subscribers, name='manage_subscribers'),
]