from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers


CustomUser = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserWriteSerializer


class LoginView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer
