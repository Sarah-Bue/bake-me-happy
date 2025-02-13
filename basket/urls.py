from django.urls import path
from . import views

urlpatterns = [
    # View Basket
    path('', views.view_basket, name='view_basket'),

    # Add to Basket
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),

    # Update Basket
    path('update/<item_id>/', views.update_basket, name='update_basket'),
]