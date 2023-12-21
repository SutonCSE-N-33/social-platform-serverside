from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate, login, logout
from .serializers import (
    LoginSerializer,
    RegistrationSerializer,
    UserSerializer,
    UserProfileSerializer,
)
from django.http import Http404, JsonResponse
from django.middleware.csrf import get_token
from .permissions import IsOwnerOnly
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from django.contrib.auth.models import User
from .models import UserProfile


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                user_profile = UserProfile.objects.get(user=user)
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "token": token.key,
                        "user_id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(
                {"detail": "Successfully logged out."}, status=status.HTTP_200_OK
            )
        except Token.DoesNotExist:
            return Response(
                {"detail": "Token does not exist."}, status=status.HTTP_404_NOT_FOUND
            )




class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            UserProfile.objects.create(user=user)
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated, IsOwnerOnly]
     serializer_class = UserProfileSerializer

     def get_queryset(self):
          if self.request.user.is_authenticated:
            return UserProfile.objects.filter(user=self.request.user)
          else:
            return UserProfile.objects.none()
       
        

class DeleteUserView(DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = "id"