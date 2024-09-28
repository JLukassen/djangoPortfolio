from django.contrib import admin

from .models import WorkExperience


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', 'start_date', 'end_date', 'description', 'image']

admin.site.register(WorkExperience, WorkExperienceAdmin)
