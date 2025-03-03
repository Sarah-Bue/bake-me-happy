from django.shortcuts import render
from .models import About


def about(request):
    """
    View to render the about page.
    """

    about = About.objects.first()
    
    # If no About object exists, create a default one
    if not about:
        about = About.objects.create(
            title="About Us",
            content="Welcome to Bake Me Happy!"
        )
    
    context = {
        'about': about,
        'on_about_page': True,
    }
    
    return render(request, 'about/about.html', context)
