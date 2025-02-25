from django.db import models

class Subscriber(models.Model):
    """
    A model to store email addresses of newsletter subscribers.
    """

    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
