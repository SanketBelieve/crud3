from django.db import models

# Create your models here.
class Player(models.Model):
    pid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    sport=models.CharField(max_length=45)
    team=models.CharField(max_length=45)
    