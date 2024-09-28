from django.db import models

class GitHubRepo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    github_url = models.URLField()
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/job_images/', blank=True, null=True)  # New image field

    def __str__(self):
        return self.name
