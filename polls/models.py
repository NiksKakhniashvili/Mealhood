from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poll(models.Model):
    garet = models.BooleanField(default=True)
    volentier = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
