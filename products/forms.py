from django import forms
from .widgets import CustomClearableFileInput

from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """Product form """

    class Meta:
        model = Product
        fields = ('category', 'sku', 'name', 'description',
                  'price', 'has_colors', 'image')

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'contact-border rounded-0'


class ReviewForm(forms.ModelForm):
    """Product form """

    class Meta:
        model = Review
        fields = ('review',)
