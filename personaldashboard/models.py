from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
# Create your models here.
class Userdetails(models.Model):
    #food
    petbottles = models.IntegerField()
    plasticbags = models.IntegerField()
    foodwrappers = models.IntegerField()
    yogurtcontainers = models.IntegerField()
    #bathroom
    detergents = models.IntegerField()
    shower = models.IntegerField()
    toohbrushes = models.IntegerField()
    toothpastes = models.IntegerField()
    #packaging
    plasticCups = models.IntegerField()
    straws = models.IntegerField()
    dispensableCutlery = models.IntegerField()
    plasticPlates = models.IntegerField()
    saved  = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
