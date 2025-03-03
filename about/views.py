from django.shortcuts import render
from .models import About, Baker


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

    bakers = Baker.objects.all()
    
    context = {
        'about': about,
        'bakers': bakers,
        'on_about_page': True,
    }
    
    return render(request, 'about/about.html', context)
