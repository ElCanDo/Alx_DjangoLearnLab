from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser

class FollowUserView(generics.GenericAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()


class UnfolowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    query_set = CustomUser.objects.all()