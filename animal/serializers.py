from .models import Animal
from rest_framework import serializers

class AnimalSerializer(serializers):
    class Meta:
        model = Animal
        fields = '__all__'
