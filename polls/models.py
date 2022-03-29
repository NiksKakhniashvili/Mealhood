from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    foods = models.CharField(max_length=100)

    def __str__(self):
        return self.foods

class Poll(models.Model):
    garet = models.BooleanField(default=True)
    volentier = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    essen = models.ForeignKey(Food,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return f'{self.user} -> {self.essen}'
    

