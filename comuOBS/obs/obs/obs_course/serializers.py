from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course  
        fields = ('url', 'id','lecturer', 'code', 'name', 'c_type', 'credit', 'ects', 'lab_hour', 'course_hour','department')