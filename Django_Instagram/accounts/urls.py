from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registerUser, name='registerUser'),
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
