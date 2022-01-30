from django.urls import path


from posts import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('createPost/', views.createPost, name='createPost'),
    path('deletePost/<str:pk>', views.deletePost, name='deletePost'),
    path('editPost/<str:pk>', views.editPost, name='editPost'),
]
