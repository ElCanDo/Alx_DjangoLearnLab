from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, pk):
        target = CustomUser.objects.get(id=pk)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target)

        return Response(
            {
                "message": "followed",
                "followed_user": {"id": target.id, "username": target.username}
            },
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, pk):
        target = CustomUser.objects.get(id=pk)
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target)

        return Response(
            {
                "message": "unfollowed",
                "unfollowed_user": {"id": target.id, "username": target.username}
            },
            status=status.HTTP_200_OK
        )