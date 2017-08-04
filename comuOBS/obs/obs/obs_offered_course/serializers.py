from .models import OfferedCourse
from rest_framework import serializers

class OfferedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferedCourse  
        fields = ('url', 'course','semester','id','active_year')