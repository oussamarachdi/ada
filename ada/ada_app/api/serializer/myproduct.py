from rest_framework import serializers
from ada_app.models import MyProduct

class MyProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct

        fields = [
            'name',
            'user'
        ]

class MyProductWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyProduct

        fields = '__all__'

