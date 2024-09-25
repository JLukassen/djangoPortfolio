from django.db import models

# Create your models here.
class SideProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)  # Optional field for live demo links

    def __str__(self):
        return self.title