from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from twitterclone.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
def notification_view(request):
    notifications = Notification.objects.all()
    # do something here to get notifications to go away once viewed
    return render(request, 'notification.html', {'notifications': notifications})
