from .models import PotholeInfo
from .serializers import PotholeInfoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PotholeList(APIView):
    """
    List all potholes, or add a new pothole.
    """
    def get(self, request, format=None):
        potholes = PotholeInfo.objects.all()
        serializer = PotholeInfoSerializer(potholes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # print(request.data)
        pothole = PotholeInfo()
        pothole.save(**request.data)
        serializer = PotholeInfoSerializer(pothole)
        return Response(serializer.data, status=status.HTTP_201_CREATED)