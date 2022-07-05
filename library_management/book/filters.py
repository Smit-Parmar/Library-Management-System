from django_filters import rest_framework as filters
from .models import Book


# We create filters for each field we want to be able to filter on
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    published_date = filters.DateTimeFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date',]

