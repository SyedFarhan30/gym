from django.db import models
from datetime import datetime

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    occupation = models.CharField(max_length=122)
    phone = models.TextField()
    weight = models.IntegerField()
    height = models.IntegerField()
    fitnessGoal = models.CharField(max_length=122)
    date = models.DateField(default= datetime.today())
    
    def __str__(self):
        return self.name
    
