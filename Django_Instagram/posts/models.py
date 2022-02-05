from django.db import models
from django.utils.safestring import mark_safe

from django.contrib.auth.models import User

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


