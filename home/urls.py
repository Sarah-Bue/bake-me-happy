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
    path(
        'manage-subscribers/',
        views.manage_subscribers,
        name='manage_subscribers'
    ),

    # Manage Reviews
    path('manage-reviews/', views.manage_reviews, name='manage_reviews'),

    # Manage Contacts
    path('manage-contacts/', views.manage_contacts, name='manage_contacts'),

    # View Contacts
    path('contact/<int:contact_id>/', views.view_contact, name='view_contact'),

    # Manage Bakers
    path('manage-bakers/', views.manage_bakers, name='manage_bakers'),

    # Manage FAQ
    path('manage-faq/', views.manage_faq, name='manage_faq'),

    # Manage Products
    path('manage-products/', views.manage_products, name='manage_products'),
]
