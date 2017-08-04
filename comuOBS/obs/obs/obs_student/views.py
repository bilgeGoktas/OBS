 

# Create your views here.
from rest_framework import viewsets 
from django.contrib.auth.models import User
from .models import Student
from .serializers import StudentSerializer,UserSerializer

class StudentViewSet(viewsets.ModelViewSet):  
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = UserSerializer

