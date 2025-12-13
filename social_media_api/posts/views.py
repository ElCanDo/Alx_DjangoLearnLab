from rest_framework import viewsets, permissions, status, generics
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from notifications.models import Noification

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Noification.objects.create(
                recipient=post.author,
                sender=request.user,
                post=post,
                notification_type='like'
            )
            return Response({'message': 'post liked'},
                            status=status.HTTP_201_CREATED
                            )
        else:
            like.delete()
            return Response({'status': 'post unliked'})


class FeedViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(feed_posts, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

