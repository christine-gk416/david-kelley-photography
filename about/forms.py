from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit ('submit', 'Send message', css_class="form-button"))
        self.helper.layout = Layout(
            Row(
                Column('name', css_class="col-lg-6"),
                Column('email', css_class="col-lg-6" ),
                css_class='form-row'),
            Row (
                Column('subject')
            ),
            Row (
                Column('message')
            )
        )

        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'contact-border rounded-0'
