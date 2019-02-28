from .models import PotholeInfo
from .serializers import PotholeInfoSerializer
from decimal import Decimal
from math import sin, cos, sqrt, atan2, radians
from rest_framework.generics import ListCreateAPIView, ListAPIView
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


class NearbyPotholeList(ListAPIView):
    """
    List all potholes, in range of 15 kms of a certain lat lang.
    """
    serializer_class = PotholeInfoSerializer
    paginate_by = 100

    def get_queryset(self):
        # This method is very hackish now, will need to change later tho. 
        lat = self.kwargs['lat']
        long = self.kwargs['long']
        lat = Decimal(lat)
        long = Decimal(long)
        
        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(lat)
        lon1 = radians(long)

        all_potholes = PotholeInfo.objects.all()
        filtered = list()
        for ph in all_potholes:

            lat2 = radians(ph.lat)
            lon2 = radians(ph.long)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c

            if Decimal(distance) < Decimal(15):
                filtered.append(ph)
                # print("Result:", distance)
        return filtered

    def list(self, request, lat=25.791400, long=85.002000):
        print(lat, long)
        queryset = self.get_queryset()
        serializer = PotholeInfoSerializer(queryset, many=True)
        return Response(serializer.data)