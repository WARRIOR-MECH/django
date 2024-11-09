from rest_framework import
from .models import Book
class Bookserializer(serializer.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'