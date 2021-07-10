from django.db import models
from hospital.models import Hospital,Department
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    degree = models.CharField(max_length=1000)
    years_of_experience = models.IntegerField(default=0)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="doctor/",blank=True,default=None)


    def __str__(self):
        return f"{self.name},{self.degree}"
