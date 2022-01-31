from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.forms import RegisterForm


# Create your views here.

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
            messages.warning(request, 'No te has identificado')

    return render(request, 'home.html')


def registerUser(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


def logoutUser(request):

    logout(request)

    return redirect('/')
