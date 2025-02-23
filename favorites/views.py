from django.shortcuts import render

def view_favorites(request):
    """
    A view to return the  favorites list page.
    """
    return render(request, 'favorites/view_favorites.html')