from django import forms
from .models import Product, Category, Occasion, Allergen
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    A form for adding and editing products.
    """

    allergens = forms.ModelMultipleChoiceField(
        help_text="Select all applicable allergens.",
        queryset=Allergen.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
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
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'step': 0.1,
            }),
        }
        help_texts = {
            'rating': 'Enter a rating between 1 and 5.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        occasions = Occasion.objects.all()

        # Create category choices list
        category_choices = [
            (c.id, c.get_friendly_name()) for c in categories
        ]
        self.fields['category'].choices = category_choices

        # Create occasion choices list
        occasion_choices = [
            (o.id, o.get_friendly_name()) for o in occasions
        ]
        self.fields['occasion'].choices = occasion_choices

        # Convert allergens list to comma-separated string for display in form
        if self.instance.pk and self.instance.allergens:
            self.initial['allergens'] = ', '.join(self.instance.allergens)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-2'
