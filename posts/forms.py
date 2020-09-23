from django import forms

from .models import Post, Salon, Adviser
from .widgets import FileInputWithPreview

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'rows':6, 'colums':40})

    class Meta:
        model = Post
        fields = ("author","salon","adviser", "picture", "picture2", "picture3", "text", "created_at")
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