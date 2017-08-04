#! -*- coding:utf-8 -*-
from django.db import models
from obs.obs_lecturer.models import Lecturer

# Create your models here.

class Advisor(models.Model):
    lecturer = models.ForeignKey(Lecturer)  
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.lecturer.user.first_name

    class Meta:
        verbose_name ="Danışman"
        verbose_name_plural="Danışmanlar"

