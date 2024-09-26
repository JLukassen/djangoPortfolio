from django.contrib import admin
from .models import GitHubRepo

class GitHubRepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'featured')  # Display featured in the list
    list_filter = ('featured',)  # Filter by featured status
    search_fields = ('name', 'description')  # Allow searching by name or description
    list_editable = ('featured',)  # Make 'featured' editable directly from the list view


admin.site.register(GitHubRepo, GitHubRepoAdmin)

