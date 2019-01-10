from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    DOB = models.DateField('date of birth')
    address = models.CharField(max_length=250)
    genger = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)


class Complains(models.Model):
    u = models.ForeignKey(User, on_delete=models.CASCADE)
    tyOfAb = models.CharField(max_length=25)
    descrip = models.CharField(max_length=500, null=True)

