from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)
class Complain(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    subject=models.CharField(max_length=200)
    complaintext=models.TextField()
    complaindate=models.CharField(max_length=20)
class Career(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    qualification=models.CharField(max_length=50)
    experince=models.CharField(max_length=10)
    keyskills=models.TextField()
    cv=models.CharField(max_length=100)
    connectdate=models.CharField(max_length=20)
class LoginInfo(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)



