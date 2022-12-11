from rest_framework import viewsets
from ..models import Library
from .serializer import SerializerLibrary


class LibraryViewSets(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = SerializerLibrary