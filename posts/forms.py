from django import forms

from .models import Post
from .widgets import FileInputWithPreview

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("picture", "text")
        widgets = {
            'picture': FileInputWithPreview,
        }