from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'accounts/register.html', {
        'title': 'Register'
    })


def loginUser(request):
    return render(request, 'accounts/login.html', {
        'title': 'login'
    })
