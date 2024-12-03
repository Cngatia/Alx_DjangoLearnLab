import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search by title
    publication_year = django_filters.NumberFilter(field_name='publication_year') 
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains') 
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']