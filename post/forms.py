
from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body']
        labels = {
            'body': 'Caption',
        }

        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption....', 'class': 'font1 text-4xl'}),
            'url': forms.URLInput(attrs={'placeholder': 'Add a url....', }),
        }


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': '',
        }

        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption....', 'class': 'font1 text-4xl'}),
        }
