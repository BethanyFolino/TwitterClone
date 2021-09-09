from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.forms import CreateTweetForm
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from twitterclone.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
@login_required
def homepage(request):
    tweets = Tweet.objects.all().order_by('-id')
    users_tweets = Tweet.objects.filter(created_by=request.user)
    tweet_count = users_tweets.count()
    return render(request, 'homepage.html', {'tweets': tweets, 'tweet_count': tweet_count})

def create_tweet(request):
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                text=data['text'],
                created_by=request.user,
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateTweetForm()
    return render(request, 'tweet_form.html', {'form': form})


def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})
