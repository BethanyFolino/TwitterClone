from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from authentication.forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from twitterclone.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            twitter_user = authenticate(request, username=data['username'], password=data['password'])
            if twitter_user:
                login(request, twitter_user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'login_form.html', {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            twitter_user1 = TwitterUser.objects.create_user(username=data['username'], password=data['password'])
            return HttpResponseRedirect(reverse('home'))
    form = SignupForm()
    return render(request, 'signup_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('home')))