from .models import Comment, Post
from django import forms
# from .widgets import CustomClearableFileInput

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')