from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# models
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

class Grade(models.Model):
    subject = models.ManyToManyField(Subject)
    score = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(9)
    ])
