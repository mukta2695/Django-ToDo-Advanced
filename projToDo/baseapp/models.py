#Importing User model which takes care of all the user info like username, email, password, etc.
from django.contrib.auth.models import User
from django.contrib.gis.db import models


# Create your models here.


class Task(models.Model):

    #Creating attributes and setting the values (ONE TO MANY Relationship) --> one user can have many items/ tasks

    #If the user gets deleted then the tasks are also deleted
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    #Title of max length 400 chars, is mandatory
    title=models.CharField(max_length=400, null=False, blank=False)
    #Description is not mandatory
    description=models.TextField(null=True, blank=True)
    #Check if the task is complete or not
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    class Meta:
        #Any completed task is sent at the bottom of the list
        ordering=['complete']

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

