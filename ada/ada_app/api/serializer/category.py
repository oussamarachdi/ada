from rest_framework import serializers
from ada_app.models import Category
from .subcategory import SubCategorySerializer
from .product import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    subcategory_set = SubCategorySerializer(many=True, read_only=True)
    product_set = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category

        fields = [
            'pk',
            'name',
            'subcategory_set',
            'product_set',
        ]

    