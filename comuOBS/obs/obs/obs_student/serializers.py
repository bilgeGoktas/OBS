from .models import Student
from django.contrib.auth.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ('url', 'id', 'user', 'gender', 'number', 'active_record_semester', 'birthdate', 'phone', 'department', 'image','join_year')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'first_name', 'last_name',)
