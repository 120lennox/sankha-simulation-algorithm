from django.db import models
from programs.models import Program
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

class Grade(models.Model):
    subject = models.ManyToManyField(Subject)
    score = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(9)
    ])
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Grade)
    program = models.ManyToManyField(Program)

    def __str__(self):
        return self.name

