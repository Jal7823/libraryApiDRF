from rest_framework import serializers
from ..models import Books,Author,Editorial,Category


class SerializerAuthor(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class SerializerEditorial(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SerializerBooks(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    editorial = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = '__all__'