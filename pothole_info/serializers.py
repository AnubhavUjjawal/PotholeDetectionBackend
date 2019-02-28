from rest_framework import serializers
from .models import PotholeInfo

class PotholeInfoSerializer(serializers.ModelSerializer):
    """Serializer for PotholeInfo models in ./models.py"""

    class Meta:
        model = PotholeInfo
        fields = '__all__'
        read_only = ['img_with_potholes']

