
from django.db import models


class About(models.Model):
    """
    Model for the About page content.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Meta class to set verbose name and plural name in admin interface
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
