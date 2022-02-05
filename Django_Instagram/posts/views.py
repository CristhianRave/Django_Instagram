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
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            data_form = form.cleaned_data
            post = Post(
                user_id=request.user.id,
                quote=request.POST.get('quote'),
                image=request.FILES.get('image'),
            )
            post.save()
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


def likePost(request, pk):
    post = Post.objects.get(id=pk)

    is_dislike = False
    for dislike in post.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break
    
    if is_dislike:
        post.dislikes.remove(request.user)

    is_like = False
    for like in post.likes.all():
        if like ==  request.user:
            is_like = True
            break

    if not is_like:
        post.likes.add(request.user)

    if is_like:
        post.likes.remove(request.user)

    return redirect(posts)



def dislikePost(request, pk):
    post = Post.objects.get(id=pk)

    is_like = False
    for like in post.likes.all():
        if like == request.user:
            is_like = True
            break

    if is_like:
        post.likes.remove(request.user)

    is_dislike = False
    for dislike in post.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break

    if not is_dislike:
        post.dislikes.add(request.user)

    if is_dislike:
        post.dislikes.remove(request.user)
    return redirect(posts)
