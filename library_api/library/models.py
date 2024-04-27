from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Category(models.Model):
  """Model for Book Categories"""
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Book(models.Model):
  """Model for Books in the Library"""
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  no_of_pages = models.IntegerField()
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
