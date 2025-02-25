from django.shortcuts import render
from django.http import JsonResponse
from .forms import NewsletterForm
from .models import Subscriber
from django.contrib import messages

def newsletter_signup(request):
    """
    A view to handle newsletter signup form submissions.
    """
    
    if request.method == 'POST':
        # Initialize form with POST data
        form = NewsletterForm(request.POST)        
        if form.is_valid():
            # Create instance but don't save yet
            instance = form.save(commit=False)
            
            # Check for duplicate email addresses
            if Subscriber.objects.filter(email=instance.email).exists():
                return JsonResponse({
                    'success': False, 
                    'message': f"{instance.email} already exists in our database."
                })
            
            # Save the new subscriber
            instance.save()
            return JsonResponse({
                'success': True,
                'message': f"{instance.email} has been added to our newsletter"
            })
            
        # Return form validation errors
        return JsonResponse({
            'success': False, 
            'errors': form.errors
        })
        
    # Return error for non-POST requests
    return JsonResponse({'success': False})