from rest_framework import viewsets 
from .models import RegisterNote
from .serializers import RegisterNoteSerializer

class RegisterNoteViewSet(viewsets.ModelViewSet):  
    queryset = RegisterNote.objects.all()
    serializer_class = RegisterNoteSerializer