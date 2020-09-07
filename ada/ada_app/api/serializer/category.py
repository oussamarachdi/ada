from rest_framework import serializers
from ada_app.models import Category
from .subcategory import SubCategoryListSerializer
from .product import ProductListSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    subcategory_set = SubCategoryListSerializer(many=True, read_only=True)
    product_set = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category

        fields = [
            'pk',
            'name',
            'subcategory_set',
            'product_set',
        ]
class CategoryWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = [
            'name',
        ]
    