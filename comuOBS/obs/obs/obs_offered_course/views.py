from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets 
from .models import OfferedCourse
from .serializers import OfferedCourseSerializer

class OfferedCourseViewSet(viewsets.ModelViewSet):  
    queryset = OfferedCourse.objects.all()
    serializer_class = OfferedCourseSerializer
