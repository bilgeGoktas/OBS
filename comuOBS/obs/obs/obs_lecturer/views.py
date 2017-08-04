from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .models import User
from .models import Lecturer
from .serializers import LecturerSerializer

class LecturerViewSet(viewsets.ModelViewSet):  
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

