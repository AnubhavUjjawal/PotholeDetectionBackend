from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import PotholeInfo

class PotholeInfoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PotholeInfo
        geo_field = "point"
        fields = ("id", "img", "danger_level", "user_feedback")

    def create(self, validated_data):
        return NotImplementedError

