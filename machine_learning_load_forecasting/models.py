from django.db import models

# Create your models here.


class Load(models.Model):
    power = models.FloatField()