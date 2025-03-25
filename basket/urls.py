from django.urls import path
from . import views


urlpatterns = [
    # View Basket
    path('', views.view_basket, name='view_basket'),

    # Add to Basket
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),

    # Update Basket
    path('update/<item_id>/', views.update_basket, name='update_basket'),

    # Remove from Basket
    path('remove/<item_id>/',
         views.remove_from_basket, name='remove_from_basket'),

    # Clear Basket
    path('clear/', views.clear_basket, name='clear_basket'),
]
