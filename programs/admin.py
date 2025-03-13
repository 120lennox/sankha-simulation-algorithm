from django.contrib import admin
from .models import Program, Requirement
from subjects.models import Subject


# admin customization
# programs/admin.py
class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1
    fk_name = 'program'
    
    # This will help show which subjects are already used
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject":
            if request.resolver_match.kwargs.get('object_id'):
                program_id = request.resolver_match.kwargs.get('object_id')
                used_subjects = Requirement.objects.filter(program_id=program_id).values_list('subject_id', flat=True)
                kwargs["queryset"] = Subject.objects.exclude(id__in=used_subjects)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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