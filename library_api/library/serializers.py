from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'  # Include all fields

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'  # Include all fields
