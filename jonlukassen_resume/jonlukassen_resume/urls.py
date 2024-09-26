from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('experience.urls')),
    path('', include('projects.urls')),
    path('', include('github.urls')),      # Correct: for GitHub
    path('', include('salesforce.urls')),  # Correct: for Salesforce
    path('', include('resume.urls')),  # Include Resume and Contact app URLs
]
