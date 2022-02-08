from django.db import models
from django.utils.safestring import mark_safe

from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.


class Post(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True)
    image = models.ImageField(null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.quote


class CommentPost(models.Model):

    comment = models.TextField()
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, blank=True, null=True, related_name='post')
    created_at = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True,blank=True, related_name='commentAuthor')
    likes = models.ManyToManyField(User, blank=True, related_name='commentLike')
    dislikes = models.ManyToManyField(User, blank=True, related_name='commentDislike')

    def __str__(self):
        return self.comment
