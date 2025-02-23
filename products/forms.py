from django import forms
from .models import Product, Category, Occasion


class ProductForm(forms.ModelForm):
    """
    A form for adding and editing products.
    """
    
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        occasions = Occasion.objects.all()

        self.fields['category'].choices = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['occasion'].choices = [(o.id, o.get_friendly_name()) for o in occasions]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-0'