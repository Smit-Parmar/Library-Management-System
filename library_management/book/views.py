from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly
from .filters import BookFilter
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = BookFilter
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    

