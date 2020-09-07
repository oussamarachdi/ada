from rest_framework import serializers
from ada_app.models import Region
from .product import ProductListSerializer

class RegionReadSerializer(serializers.ModelSerializer):
    product_set = ProductListSerializer(many=True)
    class Meta:
        model = Region

        fields = [
            'name',
            'product_set',
        ]

class RegionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region

        fields = [
            'name',
        ]