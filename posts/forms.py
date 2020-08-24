from django import forms

from .models import Post, Salon, Adviser
from .widgets import FileInputWithPreview


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("picture", "text")
        widgets = {
            'picture': FileInputWithPreview,
        }


class SalonAddForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('name', 'tel', 'zipcode', 'address1', 'address2', 'address3', 'salon_url')

class AdviserAddForm(forms.ModelForm):
    class Meta:
        model = Adviser
        fields = ('salon', 'name',  'tel', 'email')