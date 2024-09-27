from django.db import models

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/job_images/', null=True, blank=True)  # New field for images

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Introduction(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='introduction/', null=True, blank=True)  # Add image field

    def __str__(self):
        return self.title