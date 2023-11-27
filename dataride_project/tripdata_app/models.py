from django.db import models

from django.db import models

class TripData(models.Model):
    trip_duration = models.IntegerField()
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    start_station_id = models.IntegerField()
    start_station_name = models.CharField(max_length=1000)
    start_station_latitude = models.FloatField()
    start_station_longitude = models.FloatField()
    end_station_id = models.IntegerField(null=True, blank=True)  # Allowing NULL values
    end_station_name = models.CharField(max_length=1000, null=True, blank=True) 
    end_station_latitude = models.FloatField(null=True, blank=True) 
    end_station_longitude = models.FloatField(null=True, blank=True) 
    bikeid = models.IntegerField()
    usertype = models.CharField(max_length=100, choices=[
        ('Subscriber', 'Subscriber'),
        ('Customer', 'Customer')
    ])
    birth_year = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=[(0, 'Unknown'), (1, 'Male'), (2, 'Female')])

    def __str__(self):
        return f"{self.start_station_name} to {self.end_station_name if self.end_station_name else 'Unknown'}"


