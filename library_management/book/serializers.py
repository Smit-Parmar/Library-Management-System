from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Book
        fields = ('id', 'title', 'author',)
