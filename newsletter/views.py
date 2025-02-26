
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import NewsletterForm
from .models import Subscriber

def newsletter_signup(request):
    """
    A view to handle newsletter signup form submissions.
    """
    
    if request.method == 'POST':
        form = NewsletterForm(request.POST)        
        if form.is_valid():
            instance = form.save(commit=False)
            
            # Check for duplicate email addresses
            if Subscriber.objects.filter(email=instance.email).exists():
                messages.error(request, f"{instance.email} already exists in our database." [0])
                return redirect(request.META.get('HTTP_REFERER', 'home'))
            
            # Save the new subscriber
            instance.save()

            # Send confirmation email
            cust_email = instance.email
            subject = render_to_string(
                'newsletter/confirmation_emails/confirmation_email_subject.txt'
            )
            body = render_to_string(
                'newsletter/confirmation_emails/confirmation_email_body.txt',
                {'email': cust_email}
            )
            
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )

            # Success message
            messages.success(request, f"{instance.email} has been successfully added to our newsletter. Check your email for confirmation.")
            return redirect(request.META.get('HTTP_REFERER', 'home'))
            
        # Return form validation errors
        for error in list(form.errors.values())[0]:
            messages.error(request, error)
        return redirect(request.META.get('HTTP_REFERER', 'home'))
        
    # Return error for non-POST requests
    messages.error(request, "Invalid request method")
    return redirect('home')
