from rest_framework import serializers
from ada_app.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'price',
            'description',
            'isFree',
            'review',
            'creationdate',
            'subcategory'
        ]