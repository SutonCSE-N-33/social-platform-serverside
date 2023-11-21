from django.shortcuts import render
from .models import Reply
from .serializers import ReplySerializer
from rest_framework import viewsets
# Create your views here.

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
