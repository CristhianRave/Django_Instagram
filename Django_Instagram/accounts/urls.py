from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='registerUser'),
    path('logout/', views.logout_user, name='logout'),
]
