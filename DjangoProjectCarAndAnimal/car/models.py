from django.db import models

class Car(models.Model):
    car_model = models.CharField(default="Car", max_length=20)
    released_date = models.DateField()
    max_speed = models.IntegerField(default=0)
