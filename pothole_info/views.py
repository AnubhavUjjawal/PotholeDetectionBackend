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

    def get_queryset(self, pk=None):
        if pk:
            return PotholeInfo.objects.get(pk=pk)
        return PotholeInfo.objects.all()

    def list(self, request, pk=None):
        queryset = self.get_queryset(pk=pk)
        if pk:
            serializer = PotholeInfoSerializer(queryset)
        else:
            serializer = PotholeInfoSerializer(queryset, many=True)
        return Response(serializer.data)