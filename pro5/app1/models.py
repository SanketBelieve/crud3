from django.db import models

# Create your models here.
class Laptop(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    model=models.CharField(max_length=45)
    price=models.IntegerField()

    
    