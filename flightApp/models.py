from django.db import models

# Create your models here.
class Flight(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    travel_points = models.DecimalField(max_digits= 10, decimal_places= 3)
