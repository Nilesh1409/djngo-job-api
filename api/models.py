from django.db import models

# Create your models here.

# Creating Employer model
class Employer(models.Model):
    employer_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True)
    email= models.EmailField()
    password= models.CharField(max_length=32)
    phone= models.IntegerField()

# Creating Job model
class Job(models.Model):
    job_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024)
    location = models.CharField(max_length=500)
    comapny = models.CharField(max_length=256)
    added_date = models.DateTimeField(auto_now=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


