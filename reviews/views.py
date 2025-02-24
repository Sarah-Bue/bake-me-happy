from django.shortcuts import render

def view_reviews(request):
    """
    A view to return the reviews page.
    """

    return render(request, 'reviews/reviews.html')


def add_review(request):
    """
    A view to add a new review.
    """
    
    return render(request, 'reviews/add_review.html')


def edit_review(request, review_id):
    """
    A view to edit a review.
    """

    return render(request, 'reviews/edit_review.html')


def delete_review(request, review_id):
    """
    A view to delete a review.
    """
    
    return render(request, 'reviews/delete_review.html')