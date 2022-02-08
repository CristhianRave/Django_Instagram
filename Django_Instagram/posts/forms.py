from django import forms
from posts.models import Post, CommentPost


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image','quote']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({"class": "form-control"})
        self.fields['quote'].widget.attrs.update({"class": "form-control"})


class CommentPostForm(forms.ModelForm):


    class Meta:
        model = CommentPost
        fields = ['comment',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({"class": "form-control"})

