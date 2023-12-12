
from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Caption',
            'tags': 'Categoty'
        }

        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption....', 'class': 'font1 text-4xl'}),
            'url': forms.URLInput(attrs={'placeholder': 'Add a url....', }),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'text-sm'})
        }


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Category'

        }

        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption....', 'class': 'font1 text-3xl'}),
            'tags': forms.CheckboxSelectMultiple()
        }
