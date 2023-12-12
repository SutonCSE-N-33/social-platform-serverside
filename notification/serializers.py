from rest_framework import serializers
from .models import Notification,CountNotification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
class CountNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountNotification
        fields = '__all__'