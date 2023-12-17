from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from react.models import React
from reply.models import Reply
from comment.models import Comment
# Create your models here.

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField( max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    post_author = models.IntegerField(null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, blank=True, null=True)
    react = models.ForeignKey(React, on_delete=models.CASCADE, blank=True, null=True)
    background = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user_name

class CountNotification(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField()
    post_author = models.IntegerField(null=True)
    
    


