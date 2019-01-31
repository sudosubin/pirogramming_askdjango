from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }

