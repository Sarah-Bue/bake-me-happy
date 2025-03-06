from django.urls import path
from . import views

urlpatterns = [
    # About page
    path('', views.about, name='about'),

    # Edit About section
    path('edit/', views.edit_about, name='edit_about'),

    # Edit Baker profile
    path('edit_baker/<int:baker_id>/', views.edit_baker, name='edit_baker'),

    # Delete Baker profile
    path('delete_baker/<int:baker_id>/', views.delete_baker, name='delete_baker'),

    # Add Baker profile
    path('add_baker/', views.add_baker, name='add_baker'),

    # Privacy Policy
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    # Edit Privacy Policy page
    path('privacy-policy/edit/', views.edit_privacy_policy, name='edit_privacy_policy'),

    # Allergen Info
    path('allergen_info/', views.allergen_info, name='allergen_info'),

    # Edit Allergen Info page
    path('allergen_info/edit/', views.edit_allergen_info, name='edit_allergen_info'),
]
