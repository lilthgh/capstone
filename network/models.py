
from django.db import models  
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser  
class User(AbstractUser):
      pass 

class MealPlan(models.Model):  
    USER_GENDER_CHOICES = [  
        ('male', 'Male'),  
        ('female', 'Female'),  
    ]  

    ACTIVITY_LEVEL_CHOICES = [  
        ('sedentary', 'Sedentary'),  
        ('lightly_active', 'Lightly Active'),  
        ('moderately_active', 'Moderately Active'),  
        ('very_active', 'Very Active'),  
    ]  

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    weight = models.FloatField()  
    height = models.FloatField()  
    age = models.IntegerField()  
    gender = models.CharField(max_length=6, choices=USER_GENDER_CHOICES)  # Choices for gender  
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVEL_CHOICES)  # Choices for activity level  

    def __str__(self):  
        return f"Meal Plan for {self.user.username}"