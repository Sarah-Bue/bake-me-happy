from django.urls import path
from . import views

urlpatterns = [
    # About page
    path('', views.about, name='about'),

    # Edit About page
    path('edit/', views.edit_about, name='edit_about'),

    # Edit Baker profile
    path('edit_baker/<int:baker_id>/', views.edit_baker, name='edit_baker'),

    # Delete Baker profile
    path('delete_baker/<int:baker_id>/', views.delete_baker, name='delete_baker'),

    # Add Baker profile
    path('add_baker/', views.add_baker, name='add_baker'),
]
