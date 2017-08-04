from .models import EducationPlan
from rest_framework import serializers

class EducationPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationPlan 
        fields = ('url', 'department', 'semester', 'accept_date')