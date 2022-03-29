from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from . import models


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True, source="auth_token", slug_field="key"
    )

    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "token",
            "password",
            "email",
            "name",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
            "email": {"write_only": True},
        }

    def validate(self, data):
        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                {"password": "password must to be more than 7 or more characters"}
            )
        if data.get("email") == "":
            raise serializers.ValidationError({"email": "email can't be empty"})
        if not (data.get("email")):
            raise serializers.ValidationError({"email": "email is required"})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(password)
        user.save()
        token = Token(user=user)
        token.save()
        profile = models.Account(
            user=user,
            name=validated_data["name"],
        )
        profile.save()
        return user


class LoginUserSerializer(serializers.ModelSerializer):
    token = serializers.SlugRelatedField(
        read_only=True, source="auth_token", slug_field="key"
    )

    class Meta:
        model = User
        fields = ["username", "token", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"validators": [], "write_only": True},
        }

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user == None:
            raise serializers.ValidationError(
                {"error": "Invalid Username And Password"}
            )
        else:
            return user
