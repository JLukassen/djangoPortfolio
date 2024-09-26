from django.db import models

class GitHubRepo(models.Model):
    repo_id = models.IntegerField(unique=True)  # To avoid duplicates
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    github_url = models.URLField()
    featured = models.BooleanField(default=False)  # Mark as featured in the admin panel

    def __str__(self):
        return self.name
