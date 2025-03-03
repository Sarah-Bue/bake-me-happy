
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import About, Baker


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