from .models import PotholeInfo
from .serializers import PotholeInfoSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status


class PotholeList(ListCreateAPIView):
    """
    List all potholes, or add a new pothole.
    """
    serializer_class = PotholeInfoSerializer
    paginate_by = 100

    def get_queryset(self):
        return PotholeInfo.objects.all()