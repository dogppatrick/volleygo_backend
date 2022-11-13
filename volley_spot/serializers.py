from pprint import pprint
from rest_framework import serializers
from core.models import BaseModel
from volley_spot.models import Gym, Area, Region

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = tuple()

    def create(self, validated_data):
        new_instance, _ = self.Meta.model.objects.get_or_create(**validated_data)
        return new_instance

class GymSerializer(BaseSerializer):
    class Meta:
        model = Gym
        fields = (
            "name",
            "region",
            "location"
        )
        read_only_fields = ("id",)

class AreaSerializer(BaseSerializer):
    class Meta:
        model = Area
        fields = (
            "name",
            )
        read_only_fields = ("id",)

class RegionSerializer(BaseSerializer):
    class Meta:
        model = Region
        fields = (
            "name",
            "area"

        )
        read_only_fields = ("id",)
