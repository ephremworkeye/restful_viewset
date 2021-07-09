from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Pulished'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

