from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.permissions import IsAuthenticated

from ...models import Author
from ..serializer import SerializerAuthor

class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = SerializerAuthor

