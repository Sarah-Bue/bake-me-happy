
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import About, Baker, PrivacyPolicy, AllergenInfo


class AboutForm(forms.ModelForm):
    """
    Form for editing About section content with Summernote editor.
    """
    
    class Meta:
        model = About
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }


class BakerForm(forms.ModelForm):
    """
    Form for editing baker profiles with Summernote editor.
    """
    
    class Meta:
        model = Baker
        fields = ['name', 'title', 'bio', 'image', 'order']
        widgets = {
            'bio': SummernoteWidget(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PrivacyPolicyForm(forms.ModelForm):
    """
    Form for editing Privacy Policy content with Summernote editor.
    """

    class Meta:
        model = PrivacyPolicy
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }

class AllergenInfoForm(forms.ModelForm):
    """
    Form for editing Allergen Information content with Summernote editor.
    """

    class Meta:
        model = AllergenInfo
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }