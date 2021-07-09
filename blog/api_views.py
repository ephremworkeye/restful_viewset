from rest_framework import viewsets
from rest_framework import generics, serializers
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer


# class AllAuthor(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AllPost(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


