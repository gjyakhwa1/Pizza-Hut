from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['user'] = username
            login(request, user)
            return HttpResponseRedirect(reverse('pizza'))
        messages.error(request, 'Invalid username or password')
        return redirect('/')
    else:
        return render(request, 'account/loginpage.html')


def logout_view(request):
    logout(request)
    del request.session['user']
    return HttpResponseRedirect(reverse('login'))


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'account/registerpage.html', context)
