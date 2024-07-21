from django.db import models

# Create your models here.
class Mobile(models.Model):
    mid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    brand=models.CharField(max_length=45)
    price=models.IntegerField()