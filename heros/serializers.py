from rest_framework import serializers
from .models import SuperHeroe, SuperPoder

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperHeroe
        exclude = ("is_active", )
    
class SuperPoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperPoder
        exclude = ("is_active", )