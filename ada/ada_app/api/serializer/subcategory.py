from rest_framework import serializers
from ada_app.models import SubCategory
from .product import ProductSerializer

class SubCategorySerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = SubCategory

        fields = [
            'pk',
            'name',
            'product_set',
        ]
    