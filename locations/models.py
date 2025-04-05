from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the location
    description = models.TextField(blank=True, null=True)  # Description for additional info
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Latitude coordinate
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Longitude coordinate
    created_at = models.DateTimeField(auto_now_add=True)  # When the location was created

    def __str__(self):
        return self.name
