from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    Public list view using DRF generic views.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    The Complete CRUD operations with ModelViewSet
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


###      Authentication Handling   ###


class IsAuthBookListView(APIView):
    """
    Only Authenticated Users can view the list of books
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    


class AdminBookCreate(APIView):
    """
    Only  Admin users can create books
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        # Only admin users can create new model instances
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
