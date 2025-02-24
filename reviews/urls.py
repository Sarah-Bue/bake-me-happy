from django.urls import path
from . import views

urlpatterns = [
    # View Favorites
    path('', views.view_reviews, name='reviews'),

    # Add Review
    path('add_review/', views.add_review, name='add_review'),

    # Edit Review
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]