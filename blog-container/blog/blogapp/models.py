from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # For the existing rows we need some value so we did null = true   ////// null=false is default. 
    datePosted = models.DateTimeField(null=True)
    personID = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    softDelete = models.SmallIntegerField(default=0)
    file = models.ImageField(upload_to='uploads/',null=True)
# 1 person multiple blogs

    