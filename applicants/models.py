from django.db import models
from programs.models import Program
from subjects.models import Grade

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Grade)
    program = models.ManyToManyField(Program)

    def __str__(self):
        return self.name

