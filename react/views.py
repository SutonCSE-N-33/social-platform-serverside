from django.shortcuts import render
from rest_framework import viewsets
from .models import React
from .serializers import ReactSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.db import IntegrityError
from rest_framework.response import Response
# Create your views here.
class ReactViewSet(viewsets.ModelViewSet):
    queryset = React.objects.all()
    serializer_class = ReactSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "This combination already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get_queryset(self):
        return React.objects.all()