from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from twitterclone.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
def notification_view(request):
    ...
    # current logged in user can see notifications
    # notifications will go away upon page refresh?
    # need regex for finding @ symbol in tweets
    # use regex in a tweet view?
