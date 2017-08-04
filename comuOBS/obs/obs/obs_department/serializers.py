from .models import Department
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'id','department_name', 'department_code', 'department_tel','department_fax','faculty')
