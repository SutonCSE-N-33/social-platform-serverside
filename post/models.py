from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    img_url = models.URLField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    

    def __str__(self):
        return self.content


   
   
   
    

    
    
    
    

    