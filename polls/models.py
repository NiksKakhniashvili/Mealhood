from django.db import models

# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=200)
    answer = models.BooleanField(default=True)