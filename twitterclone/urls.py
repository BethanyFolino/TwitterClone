"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from twitteruser.views import homepage
# from authentication.views import login_view, logout_view

urlpatterns = [
    # path('user/<int:user_id>/', user_profile, name='userprofile'),
    # path('follow/<int:user_id>/', follow_view, name='follow'),
    # path('unfollow/<int:user_id>/', unfollow_view, name='unfollow'),
    # path('tweet/', create_tweet, name='tweet'),
    # path('tweet/<int:tweet_id/', tweet_detail, name='tweetdetail'),
    # path('', homepage, name='home'),
    path('admin/', admin.site.urls),
    # path('login/', login_view, name='login'),
    # path('signup/', signup_view, name='signup'),
    # path('logout/', logout_view, name='logout'),
]
