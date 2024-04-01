from django.db import models

class Animal(models.Model):
    specie = models.CharField(max_length=20, default="animal")
    come_from = models.CharField(max_length=20)
    live = models.CharField(max_length=50)
    are_in_danger = models.BooleanField(default=False)