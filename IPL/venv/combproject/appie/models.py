from django.db import models

# Create your models here.
class event(models.Model):
    date=models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)

class schedule(models.Model):
    date=models.CharField(max_length=15)
    matches=models.CharField(max_length=60)
    city=models.CharField(max_length=60)

