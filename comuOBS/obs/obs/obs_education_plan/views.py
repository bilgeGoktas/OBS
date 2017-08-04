from django.shortcuts import render

from rest_framework import viewsets 
from .models import EducationPlan
from .serializers import EducationPlanSerializer

class EducationPlanViewSet(viewsets.ModelViewSet):  
    queryset = EducationPlan.objects.all()
    serializer_class = EducationPlanSerializer