from django.shortcuts import render

# Create your views here
from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framwork.permissions import IsAuthenticated,IsAdminUser
class BookList(generics.ListAPIView):
  queryset = Book.objects.all(viewsets.ModelViewSet)
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class BookViewSet(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]
