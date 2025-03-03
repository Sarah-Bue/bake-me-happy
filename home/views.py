from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    """
    A view to return the index page.
    """

    return render(request, 'home/index.html')


@login_required
def store_management(request):
    """
    A view to return the store management dashboard.
    Only accessible by admins.
    """
  
    return render(request, 'home/store_management.html')