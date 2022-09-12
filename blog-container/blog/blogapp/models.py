from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
        firstname = models.CharField(max_length=30)
        lastName= models.CharField(max_length=30)

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # For the existing rows we need some value so we did null = true   ////// null=false is default. 
    datePosted = models.DateTimeField(null=True)
    personID = models.ForeignKey(Person,on_delete=models.CASCADE, default=1)
    softDelete = models.SmallIntegerField(default=0)
# 1 person multiple blogs


class Pizza(models.Model):
    type= models.CharField(max_length=30)
    pizzaName = models.CharField(max_length=30)

class Topping(models.Model):
    toppingName = models.CharField(max_length=30)
    pizzaTopping = models.ManyToManyField(Pizza)

class Student(models.Model):
    name= models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    sem = models.CharField(max_length=30)

class Committee(models.Model):
    committeName = models.CharField(max_length=30)
    Student = models.ManyToManyField(Student, through='subscription')

class Subscription(models.Model):
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE)
    committeeID = models.ForeignKey(Committee,on_delete=models.CASCADE)
    SubscriptionDate = models.DateTimeField(auto_now_add=True)

class Album(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    