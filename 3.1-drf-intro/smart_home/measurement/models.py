from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True)


class Measurement(models.Model):
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensors = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='sensor_id',
    )
