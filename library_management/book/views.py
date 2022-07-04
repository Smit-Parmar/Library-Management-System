from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filterset_class = MovieFilter
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    

    # def retrieve(self, request, *args, **kwargs):
        
    #     serializer = super(MovieViewSet, self).retrieve(request)
    #     return Response({'data': serializer.data})

    # def list(self, request, *args, **kwargs): #For setting custom response
    #     print(request.user)
        
    #     serializer = super(MovieViewSet, self).list(request)
    #     return Response({'data': serializer.data})
