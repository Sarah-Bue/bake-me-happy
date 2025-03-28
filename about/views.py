from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import About, Baker, PrivacyPolicy, AllergenInfo, FAQ
from .forms import (
    AboutForm,
    BakerForm,
    PrivacyPolicyForm,
    AllergenInfoForm,
    FAQForm,
)


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


@login_required
def edit_about(request):
    """
    View to edit About Us content.
    """

    # Only superusers can edit about content
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('about')

    about = About.objects.first()
    if not about:
        about = About.objects.create(
            title="About Us",
            content="Welcome to Bake Me Happy!"
        )

    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'About content updated successfully')
            return redirect('store_management')
        else:
            messages.error(request,
                           'Failed to update about content.'
                           'Please ensure the form is valid.')
    else:
        form = AboutForm(instance=about)
        messages.info(request, 'You are editing the About section.')

    template = 'about/edit_about.html'
    context = {
        'form': form,
        'about': about,
    }

    return render(request, template, context)


@login_required
def edit_baker(request, baker_id):
    """
    View to edit baker profiles.
    """

    # Only superusers can edit baker profiles
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('about')

    baker = get_object_or_404(Baker, id=baker_id)

    if request.method == 'POST':
        form = BakerForm(request.POST, request.FILES, instance=baker)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f"{baker.name}'s profile updated successfully")
            return redirect('manage_bakers')
        else:
            messages.error(request,
                           'Failed to update baker profile.'
                           'Please ensure the form is valid.')
    else:
        # Preopulate form & display info message
        form = BakerForm(instance=baker)
        messages.info(request, f'You are editing {baker.name}.')

    template = 'about/edit_baker.html'
    context = {
        'form': form,
        'baker': baker,
    }

    return render(request, template, context)


@login_required
def delete_baker(request, baker_id):
    """
    Delete a baker profile.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('about')

    baker = get_object_or_404(Baker, pk=baker_id)
    baker.delete()
    messages.success(request, 'Profile deleted.')
    return redirect('manage_bakers')


@login_required
def add_baker(request):
    """
    View to add a new baker profile.
    """

    # Only superusers can add baker profiles
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('about')

    if request.method == 'POST':
        form = BakerForm(request.POST, request.FILES)
        if form.is_valid():
            baker = form.save()
            messages.success(request, f"Baker {baker.name} added successfully")
            return redirect('manage_bakers')
        else:
            messages.error(request,
                           'Failed to add baker.'
                           'Please ensure the form is valid.')
    else:
        form = BakerForm()

    template = 'about/add_baker.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def privacy_policy(request):
    """
    View to render the Privacy Policy page.
    """

    policy = PrivacyPolicy.objects.first()

    # Create placeholder if polkicy unavailable
    if not policy:
        policy = PrivacyPolicy.objects.create(
            title="Privacy Policy",
            content="Our Privacy Policy will be available soon."
        )

    context = {
        'policy': policy,
    }

    return render(request, 'about/privacy_policy.html', context)


@login_required
def edit_privacy_policy(request):
    """
    View to edit the Privacy Policy content.
    """

    # Only superusers can edit privacy policy content
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('privacy_policy')

    policy = PrivacyPolicy.objects.first()
    if not policy:
        policy = PrivacyPolicy.objects.create(
            title="Privacy Policy",
            content="Our Privacy Policy will be available soon."
        )

    if request.method == 'POST':
        form = PrivacyPolicyForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            messages.success(request, 'Privacy Policy updated successfully')
            return redirect('store_management')
        else:
            messages.error(request,
                           'Failed to update the privacy policy.'
                           'Please ensure the form is valid.')
    else:
        # Prepopulate form & display info message
        form = PrivacyPolicyForm(instance=policy)
        messages.info(request, 'You are editing the privacy policy.')

    template = 'about/edit_privacy_policy.html'
    context = {
        'form': form,
        'policy': policy,
    }

    return render(request, template, context)


def allergen_info(request):
    """
    View to render the Allergen Information page.
    """

    allergen_info = AllergenInfo.objects.first()

    # Create default allergen info if none exists
    if not allergen_info:
        allergen_info = AllergenInfo.objects.create(
            title="Allergen Information",
            content="Our Allergen Information will be available soon."
        )

    context = {
        'allergen_info': allergen_info,
    }

    return render(request, 'about/allergen_info.html', context)


@login_required
def edit_allergen_info(request):
    """
    View to edit the Allergen Information content.
    """

    # Only superusers can edit allergen information
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('allergen_info')

    allergen_info = AllergenInfo.objects.first()
    if not allergen_info:
        allergen_info = AllergenInfo.objects.create(
            title="Allergen Information",
            content="Our Allergen Information will be available soon."
        )

    if request.method == 'POST':
        form = AllergenInfoForm(request.POST, instance=allergen_info)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Allergen Information updated successfully')
            return redirect('store_management')
        else:
            messages.error(request,
                           'Failed to update the allergen information.'
                           'Please ensure the form is valid.')
    else:
        # Prepopulate form & display info message
        form = AllergenInfoForm(instance=allergen_info)
        messages.info(request, 'You are editing the allergen information.')

    template = 'about/edit_allergen_info.html'
    context = {
        'form': form,
        'allergen_info': allergen_info,
    }

    return render(request, template, context)


def faq(request):
    """
    View to display FAQs.
    """

    faqs = FAQ.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'about/faq.html', context)


@login_required
def add_faq(request):
    """
    View to add a FAQ.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('manage_faq'))
        else:
            messages.error(request,
                           'Failed to add FAQ.'
                           'Please ensure the form is valid.')
    else:
        form = FAQForm()

    template = 'about/add_faq.html'
    context = {
        'form': form,
        'is_add': True,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """
    View to edit a FAQ.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated FAQ!')
            return redirect(reverse('manage_faq'))
        else:
            messages.error(request,
                           'Failed to update FAQ.'
                           'Please ensure the form is valid.')
    else:
        form = FAQForm(instance=faq)
        messages.info(request, 'You are editing a FAQ.')

    template = 'about/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
        'is_add': False,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """
    View to delete a FAQ.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ deleted!')
    return redirect(reverse('manage_faq'))
