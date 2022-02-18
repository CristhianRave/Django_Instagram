from django.shortcuts import render, redirect
from posts.models import Post, CommentPost, Image
from posts.forms import CreatePostForm, CommentPostForm
from django.contrib.auth.models import User

# Create your views here.


def posts(request):

    post = Post.objects.all().order_by('-created_at')
    comments = CommentPost.objects.filter(post=post).order_by('-created_at')

    return render(request, 'posts/posts.html', {
        'posts': post,
        'comments': comments
    })


# -----------------------------------------------------------


def post_detail(request, pk):

    post = Post.objects.get(pk=pk)
    commentForm = CommentPostForm(request.POST)
    comments = CommentPost.objects.filter(post=post).order_by('-created_at')

    return render(request, 'posts/detailPost.html', {
        'post': post,
        'form': commentForm,
        'comments': comments
    })


# -----------------------------------------------------------


def create_post(request):

    form = CreatePostForm()

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # Guardamos las multiples imagenes del post
            for f in files:
                img = Image(image=f)
                img.save()
                post.image.add(img)
            post.save()

            return redirect('posts')

    return render(request, 'posts/createPost.html', {
        'form': form
    })


# -----------------------------------------------------------


def edit_post(request, pk):

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


# -----------------------------------------------------------


def delete_post(request, pk):

    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.delete()
        return redirect('posts')

    return render(request, 'posts/deletePost.html', {
        'post': post
    })


# -----------------------------------------------------------


def like_post(request, pk):

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
        if like == request.user:
            is_like = True
            break

    if not is_like:
        post.likes.add(request.user)

    if is_like:
        post.likes.remove(request.user)

    # Redirigir a la pagina actual
    return redirect(request.META.get('HTTP_REFERER', '/'))


# -----------------------------------------------------------


def dislike_post(request, pk):
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

    return redirect(request.META.get('HTTP_REFERER', '/'))

# -----------------------------------------------------------


def comment_post(request, pk):

    post = Post.objects.get(pk=pk)
    commentForm = CommentPostForm()
    comments = CommentPost.objects.filter(post=post)

    if request.method == 'POST':
        commentForm = CommentPostForm(
            request.POST)
        if commentForm.is_valid():
            comment = CommentPost(
                comment=request.POST.get('comment'),
            )
            comment.save(False)
            comment.author_id = request.user.id
            comment.post = post
            comment.save()

        return redirect('../post/' + str(post.pk))

    return render(request, 'posts/commentPost.html', {
        'post': post,
        'form': commentForm,
        'comments': comments

    })


# -----------------------------------------------------------


def like_comment(request, pk):

    comment = CommentPost.objects.get(pk=pk)
 
    is_dislike = False
    for dislike in comment.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break

    if is_dislike:
        comment.dislikes.remove(request.user)

    is_like = False
    for like in comment.likes.all():
        if like == request.user:
            is_like = True
            break

    if not is_like:
        comment.likes.add(request.user)

    if is_like:
        comment.likes.remove(request.user)

    # Redirigir a la pagina actual
    return redirect(request.META.get('HTTP_REFERER', '/'))


# -----------------------------------------------------------


def dislike_comment(request, pk):
    comment = CommentPost.objects.get(pk=pk)

    is_like = False
    for like in comment.likes.all():
        if like == request.user:
            is_like = True
            break

    if is_like:
        comment.likes.remove(request.user)

    is_dislike = False
    for dislike in comment.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break

    if not is_dislike:
        comment.dislikes.add(request.user)

    if is_dislike:
        comment.dislikes.remove(request.user)


    return redirect(request.META.get('HTTP_REFERER', '/'))

# def reply_comment(request,pk):
#     post = Post.objects.get(pk=pk)
#     parent_comment = Post.objects.get(pk=pk)
#     form = commentForm = CommentPostForm(request.POST)

#     if commentForm.is_valid():
#         comment = form.save(commit=False)
#         comment.author_id = request.user.id
#         comment.post = post
#         comment.parent = parent_comment
#         comment.save()

#         return redirect('../post/'+ str(post.pk))


# -----------------------------------------------------------
