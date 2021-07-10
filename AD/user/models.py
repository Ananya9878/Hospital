from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.IntegerField(max_length=1000)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)