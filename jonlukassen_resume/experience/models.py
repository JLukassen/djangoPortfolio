# Create your models here.
from django.db import models

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Leave blank if still working
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
