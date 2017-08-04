from .models import Semester
from rest_framework import serializers

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('url', 'name', 'elective_credits', 'compulsory_credits','course_amount','total_elective_amount')