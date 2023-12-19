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
    

class PostDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    
    
    def get_queryset(self):
        queryset = Post.objects.all()
        post_id = self.request.query_params.get('id')
        if post_id is not None:     #user__username means=> review model a user foreign key hisebe ache, tai user r bitoror username k access korar jonno __ use kora hoi.
            queryset = queryset.filter(Post__id=post_id)  # icontains use kora hoi jate small and capital letter hole problem na hoi
        return queryset


    


    
    



