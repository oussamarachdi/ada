from rest_framework import serializers
from ada_app.models import Profile
from .product import ProductSerializer
from .myproduct import MyProductSerializer

class ProfileSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    myproduct_set = MyProductSerializer(many=True)
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
