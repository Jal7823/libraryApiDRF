from rest_framework import viewsets
from ..models import Books
from .serializer import SerializerBooks,SerializerAuthor,SerializerEditorial,SerializerCategory

class BooksViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = SerializerBooks

class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = SerializerAuthor

class EditorialViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = SerializerEditorial

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = SerializerCategory