from .forms import NewsletterForm


def render_newsletter_signup_form(request):
    """
    Render newsletter signup form across all pages
    """

    newsletter_signup_form = NewsletterForm()

    context = {
        'newsletter_signup_form': newsletter_signup_form,
    }

    return context