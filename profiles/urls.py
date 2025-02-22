from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),

    # Order History
    path('order_history/<order_number>', views.order_history, name='order_history'),

    # Delete Profile
    path('delete_profile/', views.delete_profile, name='delete_profile'),
]