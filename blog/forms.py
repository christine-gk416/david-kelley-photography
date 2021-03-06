from tempus_dominus.widgets import DatePicker

from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    """ Blog Post Form"""

    class Meta:
        model = Post
        fields = ('title', 'author_name', 'image_url',
                  'content', 'created_on', 'status')
    # Tempus Dominus date field
    created_on = forms.DateField(widget=DatePicker(options={
                'minDate': '2021-11-01',
                'maxDate': '2023-01-20',
            },
        ),
        initial='2021-11-01',
    )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image_url'].required = True
        self.fields['author_name'].required = True
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'contact-border rounded-0'


class CommentForm(forms.ModelForm):
    """ Blog Post Comment Form """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
