from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from .models import Author, Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'status', 'author']