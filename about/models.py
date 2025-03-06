from django.db import models


class About(models.Model):
    """
    Model for storing the About section content.
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


class Baker(models.Model):
    """
    Model for storing baker profile information.
    """

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='bakers/')
    order = models.PositiveIntegerField(default=0, help_text="Order in which baker appears on the page")
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class PrivacyPolicy(models.Model):
    """
    Model for storing the Privacy Policy content.
    """

    title = models.CharField(max_length=200, default="Privacy Policy")
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"


class AllergenInfo(models.Model):
    """
    Model for storing allergen information content.
    """
    
    title = models.CharField(max_length=200, default="Allergen Information")
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Allergen Information"
        verbose_name_plural = "Allergen Information"


class FAQ(models.Model):
    """
    Model for storing FAQ questions and answers.
    """
    
    question = models.CharField(max_length=500, default="Your question here")
    answer = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which FAQ appears on the page")
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['order']