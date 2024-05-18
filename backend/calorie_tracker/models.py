from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=128, null=False)
    session_cookie = models.CharField(max_length=64, null=True)
    session_expiration = models.DateTimeField(null=True, blank=True)

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food = models.CharField(max_length=100)
    protein = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    carbohydrates = models.DecimalField(max_digits=8, decimal_places=2, default=0) 
    fats = models.DecimalField(max_digits=8, decimal_places=2, default=0)