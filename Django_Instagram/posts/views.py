from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import CreatePostForm
from django.contrib.auth.models import User

# Create your views here.


def posts(request):

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts.html', {
        'posts': posts
    })


def createPost(request):

    form = CreatePostForm()
    if request.method == 'POST':
        register_form = CreatePostForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()

            return redirect('posts')

    return render(request, 'posts/createPost.html', {
        'form': form
    })


def editPost(request, pk):

    post = Post.objects.get(pk=pk)
    form = CreatePostForm(instance=post)

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request, 'posts/createPost.html', {
        'form': form
    })


def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.delete()
        return redirect('posts')

    return render(request, 'posts/deletePost.html', {
        'post': post
    })
