from django.db import models
from django.contrib.auth.models import Use

# Create our models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200,blank=True,default=None)
    state = models.CharField(max_length=200,blank=True,default=None)
    district = models.CharField(max_length=200,blank=True,default=None)
    pincode = models.IntegerField(blank=True,default=None)
    description = models.CharField(max_length=1000)
    no_of_doctors = models.IntegerField(default=0)
    no_of_beds = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="hospital/")
    def __str__(self):
        return f"{self.name},{self.address}"



class Department(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="department/")
    description = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name},{self.hospital}"

class HospitalImage(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="hospital/")
    def __str__(self):
        return f"{self.hospital},{self.picture}"

class DepartmentImage(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="department/")
    def __str__(self):
        return f"{self.department},{self.picture}"


class MessageModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    hospital = models.ForeignKey(Hospital,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=255)
    isSenderUser = models.BooleanField(blank=True,default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['timestamp']





