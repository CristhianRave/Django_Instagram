from django.urls import path


from posts import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('createPost/', views.createPost, name='createPost'),
    path('deletePost/<str:pk>', views.deletePost, name='deletePost'),
    path('editPost/<str:pk>', views.editPost, name='editPost'),
    path('like/<str:pk>', views.likePost, name='like'),
    path('dislike/<str:pk>', views.dislikePost, name='dislike'),
    path('comment/<str:pk>', views.commentPost, name='commentPost'),
]
