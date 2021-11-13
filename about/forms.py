from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
        Row(
            Column('name', css_class='col-xl-3'),
            Column('email', css_class='col-xl-3'),
            css_class='form-row')
    )
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'contact-border rounded-0'
