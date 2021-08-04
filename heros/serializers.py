from rest_framework import serializers
from .models import SuperHeroe, SuperPoder

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperHeroe
        fields = ("__all__")
    
class SuperPoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperPoder
        fields = ("__all__")