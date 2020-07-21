from django.db import models
from django.contrib.auth.models import User
class Accounts(models.Model):
    
    name=models.CharField(max_length=17)
    password=models.CharField(max_length=10)
    phoneno = models.IntegerField(primary_key=True, blank=False, null=False)

# Create your models here.
class Member(models.Model):
    room=models.ForeignKey('Room', on_delete=models.CASCADE)
    phoneno=models.CharField    (max_length=10)
    nameofmem=models.CharField(max_length=15)
class Message(models.Model):
    rmid=models.ForeignKey('Room', on_delete=models.CASCADE)
    msgfrom=models.CharField(max_length=10)
    text=models.TextField()
    msgtime=models.DateTimeField(auto_now=True)
    
class Room(models.Model):
    roomid=models.CharField(primary_key=True,max_length=5)
    roomname=models.CharField(max_length=10)

    

