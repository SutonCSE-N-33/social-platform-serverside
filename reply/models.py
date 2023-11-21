from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from comment.models import Comment
# Create your models here.

class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    
    def __str__(self):
        return self.content