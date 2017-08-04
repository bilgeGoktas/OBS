from .models import User
from .models import Lecturer
from rest_framework import serializers

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer  
        fields = ('url', 'user', 'degree', 'room_number','phone','fax', 'address', 'gender', 'image','department','id',)
