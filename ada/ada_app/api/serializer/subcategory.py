from rest_framework import serializers
from ada_app.models import SubCategory
from .product import ProductListSerializer

class SubCategoryListSerializer(serializers.ModelSerializer):
    product_set = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory

        fields = [
            'pk',
            'name',
            'product_set',
        ]
    
class SubCategoryWriteSerializer(serializers.ModelSerializer):

    class Meta :
        model = SubCategory

        fields = [
            'name',
        ]