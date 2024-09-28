from django.shortcuts import render
from .models import GitHubRepo

# View to list featured GitHub repositories
def featured_repos(request):
    # Fetch all featured repositories
    repos = GitHubRepo.objects.filter(featured=True)
    return render(request, 'github/featured_repos.html', {'repos': repos})