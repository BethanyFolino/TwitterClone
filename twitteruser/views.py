from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from twitterclone.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
def user_profile(request, id):
    tweets = Tweet.objects.all().order_by('-id')
    twitter_user = TwitterUser.objects.get(id=id)
    users_tweets = Tweet.objects.filter(created_by=twitter_user)
    tweet_count = users_tweets.count()
    return render(request, 'user_profile.html', {'twitter_user': twitter_user, 'tweets': tweets, 'tweet_count': tweet_count})

def follow_view(request, id):
    user_to_follow = TwitterUser.objects.get(id=id)
    request.user.following.add(user_to_follow)
    request.user.save()
    return HttpResponseRedirect(reverse('home'))

def unfollow_view(request, id):
    user_to_follow = TwitterUser.objects.get(id=id)
    request.user.following.remove(user_to_follow)
    request.user.save()
    return HttpResponseRedirect(reverse('home'))
