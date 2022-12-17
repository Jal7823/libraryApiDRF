from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.permissions import IsAuthenticated

from ...models import Books
from ..serializer import SerializerBooks

class BooksViewSets(viewsets.ModelViewSet): 
    permission_classes = [IsAuthenticated]
    queryset = Books.objects.all()
    serializer_class = SerializerBooks

