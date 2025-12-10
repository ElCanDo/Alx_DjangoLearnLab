from django.shortcuts import render
from rest_framework.views import viewsets
from .serializer import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.iobjects.all()
    serializer_class = CommentSerializer
