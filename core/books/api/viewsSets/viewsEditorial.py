from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.permissions import IsAuthenticated

from ...models import Editorial
from ..serializer import SerializerBooks,SerializerAuthor,SerializerEditorial,SerializerCategory

class EditorialViewSets(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = SerializerEditorial
