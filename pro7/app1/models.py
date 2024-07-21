from django.db import models

# Create your models here.
class Football(models.Model):
    cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    country=models.CharField(max_length=45)
    city=models.CharField(max_length=45)