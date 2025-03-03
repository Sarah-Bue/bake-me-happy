
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import About


class AboutForm(forms.ModelForm):
    """
    Form for editing the About page content with Summernote editor.
    """
    
    class Meta:
        model = About
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
