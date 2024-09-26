from django.contrib import admin
from .models import GitHubRepo

class GitHubRepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'featured')

admin.site.register(GitHubRepo, GitHubRepoAdmin)
