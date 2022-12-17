from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.permissions import IsAuthenticated

from ...models import Category
from ..serializer import SerializerCategory

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = SerializerCategory