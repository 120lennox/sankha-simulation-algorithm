from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    program = models.CharField(max_length=200) # will have to change this