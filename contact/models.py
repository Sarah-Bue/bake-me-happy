from django.db import models


class Contact(models.Model):
    """
    Model to store contact form messages.
    """

    # Fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    # Automatic time stamp
    date_sent = models.DateTimeField(auto_now_add=True)

    # Default ordering by date_sent
    class Meta:
        ordering = ['-date_sent']

    # String representation
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
