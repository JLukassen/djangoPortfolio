import requests
from django.core.management.base import BaseCommand
from github.models import GitHubRepo

class Command(BaseCommand):
    help = 'Fetch repositories from GitHub and save them to the database'

    def handle(self, *args, **kwargs):
        username = 'your_github_username'  # Replace with your GitHub username
        url = f'https://api.github.com/users/JLukassen/repos'
        response = requests.get(url)

        if response.status_code == 200:
            repos_data = response.json()

            for repo_data in repos_data:
                repo, created = GitHubRepo.objects.get_or_create(
                    repo_id=repo_data['id'],
                    defaults={
                        'name': repo_data['name'],
                        'description': repo_data['description'],
                        'github_url': repo_data['html_url'],
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Repository '{repo.name}' added."))
                else:
                    self.stdout.write(self.style.WARNING(f"Repository '{repo.name}' already exists."))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch GitHub repositories.'))
