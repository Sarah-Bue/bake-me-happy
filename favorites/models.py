from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favorite(models.Model):
    """
    Model to represent user favorites.
    """

    # Link to User and Product models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Create time stamp for favorite
    date_added = models.DateTimeField(auto_now_add=True)

    # Ensure uniqueness of user-product pair to prevent duplicates
    class Meta:
        unique_together = ['user', 'product']

    # String representation of the favorite
    def __str__(self):
        return f"{self.user.username}'s favorite - {self.product.name}"
