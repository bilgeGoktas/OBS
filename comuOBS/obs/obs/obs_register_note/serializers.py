from .models import RegisterNote
from rest_framework import serializers

class RegisterNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterNote
        fields = ('url','id','register','mid_exam', 'final_exam', 'make_up_exam','make_up_exam_status','success')
