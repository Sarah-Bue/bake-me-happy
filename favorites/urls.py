from django.urls import path
from . import views

urlpatterns = [
    # View Favorites
    path('', views.view_favorites, name='favorites'),

    # Toggle Favorites
    path('toggle/<int:product_id>/', views.toggle_favorites, name='toggle_favorites'),
]