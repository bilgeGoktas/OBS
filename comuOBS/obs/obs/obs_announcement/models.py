#! -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Announcement(models.Model):
    created_date = models.CharField(max_length=50)
    finish_date = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=1000)
    
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Duyuru"
        verbose_name_plural="Duyurular"

