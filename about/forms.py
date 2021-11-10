from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        Div(
            Field('name', wrapper_class='col-xl-6 mb-0'),
            Field('email', wrapper_classs='col-xl-6 mb-0'),
        )
    )
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'contact-border rounded-0'
