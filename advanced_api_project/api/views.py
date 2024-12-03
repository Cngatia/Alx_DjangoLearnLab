from django.shortcuts import render
from rest_framework import viewsets
from .models import Book,Author
from .serializers import BookSerializer,AuthorSerializer
from django_filters import rest_framework
# class Bookviewset(viewsets.ModelViewSet):
#   queryset = Book.objects.all()
#   serializer_class = BookSerializer
# class Authorviewset(viewsets.ModelViewSet):
#   queryset = Author.objects.all()
#   serializer_class = AuthorSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated,AllowAny
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from rest_framework import filters
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = BookFilter
    search_fields = [filters.SearchFilter]
    filter_backends =  [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or publication year
    ordering = ['title']  # Default ordering (can be adjusted)
    search_fields = ['title', "author"]

class BookCreateView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticated]
class BookDetailView(RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[AllowAny]
class BookUpdateView(UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticated]
class BookDeleteView(DestroyAPIView): 
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticated]