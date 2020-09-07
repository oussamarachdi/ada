from rest_framework import serializers
from ada_app.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region

        fields = [
            'name',
        ]

