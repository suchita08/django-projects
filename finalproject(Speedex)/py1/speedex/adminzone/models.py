from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationtext=models.TextField()
    posteddate=models.CharField(max_length=20)
class City(models.Model):
    cityname=models.CharField(max_length=200)
class Consignment(models.Model):
    refno=models.CharField(max_length=50,primary_key=True)
    sendername=models.CharField(max_length=50)
    senderaddress=models.TextField()
    sendercontactno = models.CharField(max_length=15)
    receivername=models.CharField(max_length=50)
    receiveraddress=models.TextField()
    source=models.CharField(max_length=200)
    currentcity=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    status=models.CharField(max_length=20)
    posteddate=models.CharField(max_length=30)

