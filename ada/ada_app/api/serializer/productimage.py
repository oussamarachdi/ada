from rest_framework import serializers
from ada_app.models import ProductImage


class ProductImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'name',
            'File',
        ]

class ProductImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'name',
            'File',
        ]
