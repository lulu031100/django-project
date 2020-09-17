from django import forms

from .models import Post, Salon, Adviser
from .widgets import FileInputWithPreview

class PostForm(forms.ModelForm):
    salon = forms.ModelChoiceField(
        queryset= Salon.objects,
        required=False)
    class Meta:
        model = Post
        fields = ("picture", "picture2", "picture3", "text", "author", "adviser", "salon", "created_at")
        widgets = {
            'picture': FileInputWithPreview,
            'picture2': FileInputWithPreview,
            'picture3': FileInputWithPreview,
        }

class SalonAddForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('name', 'tel', 'zipcode', 'address1', 'address2', 'address3', 'salon_url')

class AdviserAddForm(forms.ModelForm):
    class Meta:
        model = Adviser
        fields = ('salon', 'name',  'tel', 'email')