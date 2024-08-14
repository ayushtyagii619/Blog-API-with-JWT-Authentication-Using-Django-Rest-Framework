from django.shortcuts import render
from .models import Category,Post,Comment
from .serializers import CategoryReadSerializer,PostReadSerializer,PostWriteSerializer,CommentReadSerializer,CommentWriteSerializer
from .permissions import IsAuthororReadOnly
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status,settings,viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryReadSerializer
    permission_classes = [AllowAny]

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    def get_serializer_class(self):
        if self.action in ("create","update","partial_update","destroy"):
            return PostWriteSerializer
        return PostReadSerializer
    
    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ("update","partial_update","destroy"):
            self.permission_classes = [IsAuthororReadOnly]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_queryset(self):
        res = super().get_queryset()
        post_id = self.kwargs.get("post_id")
        return res.filter(post__id = post_id)

    def get_serializer_class(self):
        if self.action in ("create","update","partial_update","destroy"):
            return CommentWriteSerializer
        return CommentReadSerializer
    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ("update","partial_update","destroy"):
            self.permission_classes = [IsAuthororReadOnly]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

class LikeApiView(APIView):
    def get(self,request,pk):
        user = request.user
        post = get_object_or_404(Post,pk=pk)
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        return Response({"liked": not user in post.likes.all()},status=status.HTTP_200_OK)

# Create your views here.
