from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    company=models.CharField(max_length=45)
    designation=models.CharField(max_length=45)
