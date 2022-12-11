from rest_framework import serializers
from ..models import Library

class SerializerLibrary(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    class Meta:
        model = Library
        fields = '__all__'