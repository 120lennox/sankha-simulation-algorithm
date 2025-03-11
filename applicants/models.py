from django.db import models
from programs.models import Program
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(9)
    ])
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)
    program = models.ManyToManyField(Program)

    def __str__(self):
        return self.name

