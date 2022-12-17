from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.permissions import IsAuthenticated

from ...models import Books,Author
from ..serializer import SerializerBooks,SerializerAuthor,SerializerEditorial,SerializerCategory

class BooksViewSets(viewsets.ModelViewSet): 
    permission_classes = [IsAuthenticated]
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