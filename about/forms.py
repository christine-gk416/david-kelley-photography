from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    
    helper = FormHelper()
    helper.layout = Layout(
    Div(
        Field('name', wrapper_class='col-xl-6'),
        Field('email', wrapper_classs='col-xl-6'),
        css_class='form-row')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'contact-border rounded-0'
