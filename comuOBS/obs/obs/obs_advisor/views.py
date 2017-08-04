from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets 
from .models import Advisor
from .serializers import AdvisorSerializer

class AdvisorViewSet(viewsets.ModelViewSet):  
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
