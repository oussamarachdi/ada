from rest_framework import serializers
from ada_app.models import Profile
from .product import ProductListSerializer
from .myproduct import MyProductListSerializer

class ProfileListSerializer(serializers.ModelSerializer):
    product_set = ProductListSerializer(many=True, read_only=True)
    myproduct_set = MyProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Profile

        fields = [
            'user',
            'name',
            'email',
            'phone',
            'language',
            'product_set',
            'myproduct_set',
        ]

class ProfileWriteSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Profile

        fields = '__all__'