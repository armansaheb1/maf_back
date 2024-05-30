from rest_framework import serializers
from .models import ZodiacGameStatus

class ZodiacgameStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZodiacGameStatus
        fields = '__all__'