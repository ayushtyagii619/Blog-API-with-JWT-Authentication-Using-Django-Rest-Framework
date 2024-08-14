from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser, profile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","username","email")

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","username","email","password","is_staff")
        extra_kwargs = {"password":{"write_only":True}}
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ("email","password")
    def validate(self,attrs):
        user = authenticate(email=attrs.get('email'),password = attrs.get('password'))
        if not user or not user.is_active:
            raise serializers.ValidationError('Inavlid email or password')
        return user


class UserProfileSerializer(CustomUserSerializer):
    class Meta:
        model = profile
        fields = ("bio",)

class UserAvtarSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ("avtar",)
