from rest_framework import generics
from .models import Book
from .serializers import BookSerializers
class BookListCreate(generics.ListCreateAPIView):
    queryset = BookSerializers

    class BookDetail(generics.RetriveUpdateDestroyAPIView):
        queryset = Book.object.all()
        serializer_class = BookSerializer
        
