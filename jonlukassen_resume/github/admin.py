from django.contrib import admin
from .models import GitHubRepo

# Custom action to mark selected repos as featured
def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)
    modeladmin.message_user(request, "Selected repositories have been marked as featured.")

make_featured.short_description = "Mark selected repositories as featured"

def remove_featured(modeladmin, request, queryset):
    queryset.update(featured=False)
    modeladmin.message_user(request, "Selected repositories have been unmarked as featured.")

remove_featured.short_description = "Unmark selected repositories as featured"

# Register the model with custom actions
@admin.register(GitHubRepo)
class GitHubRepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'github_url', 'featured')
    list_filter = ('featured',)  # Filter by featured status
    actions = [make_featured, remove_featured]  # Add actions to the admin interface
