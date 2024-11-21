from django.db import models

# # Create your models here.
# class Courses(models.Model):
#     name=models.CharField(max_length=50)
#     duration=models.CharField(max_length=60)
#     price=models.IntegerField()

class Student(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField()
    contact=models.CharField(max_length=90)
    message=models.TextField()    
