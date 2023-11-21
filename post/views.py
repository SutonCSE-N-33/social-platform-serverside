from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.db import IntegrityError
from rest_framework.response import Response

# for api
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.db.models import Prefetch


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


    
    



