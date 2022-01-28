from django.shortcuts import render
from posts.models import Post

# Create your views here.


def posts (request):

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts.html', {
        'posts': posts
    })