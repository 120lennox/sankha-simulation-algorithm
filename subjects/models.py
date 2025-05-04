from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# models
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, default="English")

    def __str__(self):
        return self.name

class Grade(models.Model):
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(9)
    ], 
    null= True
    )

    def __str__(self):
        return f"{self.subject} (grade: {self.score})"
