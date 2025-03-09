from django import forms
from .models import Product, Category, Occasion
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    A form for adding and editing products.
    """

    allergens = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text="Enter allergens separated by commas (required)."
    )

    serving_size = forms.CharField(
        required=True,
        max_length=50,
        help_text="Enter serving size in grams (required)."
    )
    
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'image': CustomClearableFileInput(),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        occasions = Occasion.objects.all()

        self.fields['category'].choices = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['occasion'].choices = [(o.id, o.get_friendly_name()) for o in occasions]

        # Convert allergens list to comma-separated string for display in form
        if self.instance.pk and self.instance.allergens:
            self.initial['allergens'] = ', '.join(self.instance.allergens)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-2'