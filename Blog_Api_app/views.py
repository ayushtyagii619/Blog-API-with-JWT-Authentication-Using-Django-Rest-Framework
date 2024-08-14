from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer,UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserAvtarSerializer
from .models import profile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView

class UserApiView(RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

class UserRegistrationApiView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
    def post(self,request,*args,**kwargs):
        serializer  = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #token= RefreshToken.for_user
        data = serializer.data
        #data["tokens"] = {"refresh":str(token),"access":str(token.access_token)}
        return Response(data,status=status.HTTP_200_OK)

class UserLoginApiView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token= RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh":str(token),"access":str(token.access_token)}
        return Response(data,status=status.HTTP_200_OK)
    
class UserLogoutApiView(GenericAPIView):
    def post(self,request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserApiView(RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user
    
class UserProfileApiView(RetrieveUpdateAPIView):
    queryset = profile.objects.all()
    serializer_class = UserProfileSerializer
    def get_object(self):
        return self.request.user.profile

class UserAvtarApiView(RetrieveUpdateAPIView):
    queryset = profile.objects.all()
    serializer_class = UserAvtarSerializer
    def get_object(self):
        return self.request.user.profile


