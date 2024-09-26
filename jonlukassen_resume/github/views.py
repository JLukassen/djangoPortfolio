from django.shortcuts import render
from .models import GitHubRepo

def github_repos(request):
    featured_repos = GitHubRepo.objects.filter(featured=True)  # Fetch only featured repos
    return render(request, 'github/github_repos.html', {'repos': featured_repos})
