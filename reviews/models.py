from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """
    Model for product reviews.
    
    Stores review information including the product, author, rating,
    comment, and timestamps.
    """
    
    # Fields
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
    )
    review_comment = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['-date_added']

    # String method to return review information    
    def __str__(self):
        return f'Review for {self.product.name} by {self.author.username}'

