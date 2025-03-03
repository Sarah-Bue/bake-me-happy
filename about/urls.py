from django.urls import path
from . import views

urlpatterns = [
    # About page
    path('', views.about, name='about'),

    # Edit About page
    path('edit/', views.edit_about, name='edit_about'),

    # Edit Baker profiles
    path('edit_baker/<int:baker_id>/', views.edit_baker, name='edit_baker'),
]
