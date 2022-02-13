from django.urls import path

from posts import views

urlpatterns = [
    path('posts/', views.posts, name = 'posts'), 
    path('post/<str:pk>', views.post_detail, name = 'postDetail'), 
    path('createPost/', views.create_post, name = 'createPost'), 
    path('editPost/<str:pk> ', views.edit_post, name = 'editPost'), 
    path('deletePost/<str:pk> ', views.delete_post, name = 'deletePost'), 
    path('like/<str:pk> ', views.like_post, name = 'like'), 
    path('dislike/<str:pk> ', views.dislike_post, name = 'dislike'), 
    path('comment/<str:pk> ', views.comment_post, name = 'commentPost'), 
]
