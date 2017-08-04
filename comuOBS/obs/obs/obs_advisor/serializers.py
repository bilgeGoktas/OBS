from .models import Advisor
from rest_framework import serializers

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor  
        fields = ('url','id', 'lecturer', 'year')