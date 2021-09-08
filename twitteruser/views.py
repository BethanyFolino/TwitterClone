from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from twitterclone.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
def user_profile(request, id):
    twitter_user = TwitterUser.objects.get(id=id)
    return render(request, 'user_profile.html', {'twitter_user': twitter_user})

def follow_view(request, id):
    ...

def unfollow_view(request, id):
    ...
