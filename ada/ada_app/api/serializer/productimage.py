from rest_framework import serializers
from ada_app.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'name',
            'File',
        ]
