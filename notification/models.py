from django.db import models
from django.contrib.auth.models import AbstractUser
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.
class Notification(models.Model):
    message = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True, related_name='message')
    user_to_notify = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True, related_name='user_to_notify')
    new_choices = [(1, 'True'), (2, 'False')]
    new = models.BooleanField(choices=new_choices, default=1)

    def __str__(self):
        return self.user_to_notify