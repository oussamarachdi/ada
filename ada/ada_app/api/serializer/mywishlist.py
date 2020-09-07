from rest_framework import serializers
from ada_app.models import MyWishList

class MyWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWishList

        fields = [
            'user',
            'name',
            'products'
        ]