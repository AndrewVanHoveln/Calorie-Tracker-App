from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FoodEntry(models.Model):
    foodName = models.CharField(max_length = 100)
    carbs = models.DecimalField(max_digits = 6, decimal_places = 2)
    protien = models.DecimalField(max_digits = 6, decimal_places = 2)
    fats = models.DecimalField(max_digits = 6, decimal_places = 2)
    calories = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.foodName
