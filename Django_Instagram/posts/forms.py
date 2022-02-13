from django import forms
from posts.models import Post, CommentPost


class CreatePostForm(forms.ModelForm):

    quote = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'
            }),
            required=True
    )

    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'multiple' : True
            }),
            required=False
    )

    class Meta:
        model = Post
        fields = ['quote']

# Otra forma de asignar valores css/bootstrap a CreatePostForm
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['image'].widget.attrs.update({"class": "form-control"})
    #     self.fields['quote'].widget.attrs.update({"class": "form-control"})


class CommentPostForm(forms.ModelForm):

    class Meta:
        model = CommentPost
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({
            "class": "form-control",
            "rows" : 3,
            "placeholder" : "Escribe tu comentario"
            })

