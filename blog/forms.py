from turtle import width
from .models import Comment, Post
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'date_posted', 'content', 'author',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'date_posted': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date posted'}),
            'content': RichTextFormField(config_name='default'),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')