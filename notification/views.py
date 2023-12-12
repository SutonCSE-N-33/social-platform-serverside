from django.shortcuts import render
from .models import Notification, CountNotification
from .serializers import NotificationSerializer, CountNotificationSerializer
from rest_framework import viewsets
# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
class CountNotificationViewSet(viewsets.ModelViewSet):
    queryset = CountNotification.objects.all()
    serializer_class = CountNotificationSerializer
