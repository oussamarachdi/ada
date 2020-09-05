from rest_framework import serializers

from ada_app.models import (Product,
                            ProductImage,
                            SubCategory,
                            Category,
                            Profile,
                            Region,
                            MyWishList,
                            MyProduct)

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'price',
            'description',
            'isFree',
            'review',
            'creationdate'
        ]
        read_only_field = ['user']

    def get_url(self, obj):
        return obj.get_api_url()

    def validate_name(self, value):
        qs = Product.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("the title must be unique")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = [
            'pk',
            'name',
            'product',
        ]

class MyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct

        fields = [
            'name',
            'user'
        ]

class MyWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWishList

        fields = [
            'user',
            'name',
            'products'
        ]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'name',
            'File',
        ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = [
            'user',
            'name',
            'email',
            'phone',
            'language',
        ]

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region

        fields = [
            'name',
        ]

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory

        fields = [
            'name',
        ]
