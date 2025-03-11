from django.db import models
from subjects.models import Subject


# Create your models here.
class Requirement(models.Model):
    subject = models.ManyToManyField(Subject)

    
class Program(models.Model):
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 
