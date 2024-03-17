from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from .serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer


