from django.db import models
from django.db.models.fields import CharField
# Create your models here.

class UserData(models.Model):
    email=models.CharField(max_length=100) #stores the email id of the user
    pwd=models.CharField(max_length=100) #stores the hash value
    failedAttempts=models.IntegerField() #can be >=0 and <=2
    lastLoginTime=models.CharField(max_length=100) #timestamp of the 3rd unsuccessful login

