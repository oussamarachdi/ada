from rest_framework import serializers
from ada_app.models import MyProduct

class MyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct

        fields = [
            'name',
            'user'
        ]