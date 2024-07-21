from django.db import models

# Create your models here.
class Order(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    descrption=models.TextField()
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField()