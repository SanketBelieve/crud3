from django.db import models

# Create your models here.
class Bank(models.Model):
    bid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    adhar_no=models.CharField(max_length=12)
    age=models.IntegerField()
    city=models.CharField(max_length=30)