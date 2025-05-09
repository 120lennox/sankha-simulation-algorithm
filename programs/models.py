from django.db import models
from subjects.models import Subject


# Create your models here.
class Requirement(models.Model):
    GRADE_CHOICES = [(i, str(i)) for i in range(1, 10)]

    program = models.ForeignKey('Program', null=True, on_delete=models.CASCADE, related_name='subject_requirements')
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    max_grade = models.IntegerField(
        default = 6,
        choices=GRADE_CHOICES, 
        help_text="Maximum acceptable grade for this subject"
    )

    def __str__(self):
        return f"{self.subject.name} (max grade: {self.max_grade})"
    
    class Meta:
        # unique_together = ['program', 'subject']
        pass

    
class Program(models.Model):
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
 
