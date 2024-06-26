from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    # returns string representation of a particular object. normall in Python
    def __str__(self):
       return f"{self.city} ({self.code}) " 

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
       return f"{self.id}: {self.origin} to {self.destination}" 

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration > 0
