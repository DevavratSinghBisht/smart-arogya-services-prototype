from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=30)