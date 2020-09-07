from rest_framework import serializers
from ada_app.models import Product

class ProductListSerializer(serializers.ModelSerializer):
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
        ]

class ProductWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = '__all__'
        