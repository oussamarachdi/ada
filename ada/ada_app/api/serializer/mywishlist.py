from rest_framework import serializers
from ada_app.models import MyWishList

class MyWishListReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWishList

        fields = [
            'user',
            'name',
            'products'
        ]

class MyWishListWriteSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'

