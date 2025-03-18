from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    """
    View to handle the contact form submissions.
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Send email notification
            sender_name = contact_message.name
            sender_email = contact_message.email
            subject = contact_message.subject
            message = contact_message.message

            # Get admin email
            recipient = settings.DEFAULT_FROM_EMAIL

            # Send email to admin
            body = (
                f"""Name: {sender_name}
                Email: {sender_email}
                Message:{message}"""
            )
            send_mail(
                f"Contact Form: {subject}",
                body,
                sender_email,
                [recipient],
                fail_silently=False,
            )

            messages.success(request,
                             'Thank you for your message!'
                             'We will respond as soon as possible.')
            return redirect('contact')
        else:
            messages.error(request,
                           'There was an error with your form.'
                           'Please check and try again.')
    else:
        form = ContactForm()

    # Prepare context for the template
    context = {
        'form': form,
        'title': 'Contact Us',
    }

    # Render the contact page
    return render(request, 'contact/contact.html', context)
