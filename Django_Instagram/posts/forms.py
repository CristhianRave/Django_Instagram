from django import forms
from posts.models import Post


class createPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image','quote']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({"class": "form-control"})
        self.fields['quote'].widget.attrs.update({"class": "form-control"})
