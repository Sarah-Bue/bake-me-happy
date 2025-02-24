from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


def view_reviews(request):
    """
    A view to return the user's reviews page.
    """

    reviews = Review.objects.filter(author=request.user)

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """
    A view to add a new review.
    """

    product = get_object_or_404(Product, pk=product_id)
    user_review = Review.objects.filter(
        author=request.user, product=product)

    # Prevent duplicate submissions
    if user_review:
        messages.error(request,
                       'You have already submitted a review for this product.')
        return redirect(reverse('product_detail', args=[product.id]))
    

    if request.method == 'POST':
        # Handle form submission
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            form.save()
            messages.success(request, 'Your product review has been submitted.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # Error handling for invalid form
            messages.error(request, 'Failed to submit the review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    # Prepar template and context
    template = 'reviews/add_review.html'
    context = {
        'product': product,
        'form': form,
    }

    # Render the template
    return render(request, template, context)
    

@login_required
def edit_review(request, review_id):
    """
    A view to edit a review.
    """

    review = get_object_or_404(Review, pk=review_id)

    # Verify the review belongs to the user
    if request.user!= review.author:
        messages.error(request, 'Sorry, you can only edit your own reviews.')
        return redirect(reverse('reviews'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your review.')
            return redirect(reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your review for {review.product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product': review.product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    A view to delete a review.
    """

    review = get_object_or_404(Review, pk=review_id)

    # Verify the review belongs to the user
    if request.user!= review.author:
        messages.error(request, 'Sorry, you can only delete your own reviews.')
        return redirect(reverse('reviews'))


    review.delete()
    messages.success(request, 'Your review has been deleted.')
    return redirect(reverse('reviews'))