from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

