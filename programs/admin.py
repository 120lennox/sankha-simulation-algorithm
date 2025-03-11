from django.contrib import admin
from .models import Program, Requirement


# admin customization
class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1  # Number of empty forms to display
    fk_name = 'program'

class RequirementAdmin(admin.ModelAdmin):
    list_display = ['program', 'subject', 'max_grade']
    list_filter = ['program', 'subject']
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'name')
    search_fields = ['course_code', 'name']
    inlines = [RequirementInline]

# Register your models here.
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Program, ProgramAdmin)
