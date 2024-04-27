from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer

# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
