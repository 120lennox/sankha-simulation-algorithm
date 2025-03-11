from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Program(models.Model):
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 
