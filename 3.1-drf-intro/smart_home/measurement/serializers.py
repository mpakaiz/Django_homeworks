from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensors', 'temperature', 'created_at']


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = (['temperature', 'created_at'])

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = (['id', 'name', 'description', 'measurements'])

