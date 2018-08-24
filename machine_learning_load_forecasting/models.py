from django.db import models

# Create your models here.


class Load(models.Model):
    power = models.FloatField()
    date = models.CharField(max_length=100, default='')
    time = models.CharField(max_length=100, default='')
