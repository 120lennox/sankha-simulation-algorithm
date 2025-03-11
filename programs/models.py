from django.db import models


# Create your models here.
class Requirement(models.Model):
    subject = models.CharField(unique=True, blank=False, max_length=100)
    restriction = 
class Program(models.Model):
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 
