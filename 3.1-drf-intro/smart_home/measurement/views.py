# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementsSerializer, MeasurementSerializer, SensorSerializer


class ListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        data = request.data
        print(data)
        return Response({'status': 'OK'})

class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_fields = 'id'

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            mydata = response.data

            from django.core.cache import cache
            cache.set(f'ID: {mydata.get("id", None)}', {
                      'description': mydata['description']
            })
        return response

class CreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensors = Sensor.objects.filter(id=self.request.data.get('sensors'))
        print(f'sensors: {sensors}')
        serializer.save(temperature=self.request.data.get('temperature'), sensors=sensors.first())
        return Response({'status': 'OK'})

