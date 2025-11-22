from django.urls import path, include
from rest_framework.router import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path("api/books", BookList.as_view(), 
         name='book_list'),
    #The router URLs included for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
    # This includes all routes registered with the router
]