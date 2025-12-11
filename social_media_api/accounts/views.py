from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response

class FollowUserView(generics.GenericAPIView):
    permission_class = [permissions.IsAuthenticated]


class UnfolowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    