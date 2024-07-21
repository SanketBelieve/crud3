from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    std=models.CharField(max_length=10)
    grade=models.CharField(max_length=5)
    age=models.IntegerField()