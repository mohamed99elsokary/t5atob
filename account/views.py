from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from . import serializers, models

# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = serializers.RegisterUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login(request):
    serializer = serializers.LoginUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status=status.HTTP_200_OK)
