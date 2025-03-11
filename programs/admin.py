from django.contrib import admin
from .models import Program, Requirement

# Register your models here.
admin.site.register(Requirement)
admin.site.register(Program)
