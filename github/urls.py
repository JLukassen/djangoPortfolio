from django.urls import path
from . import views

urlpatterns = [
    path('', views.featured_repos, name='featured_repos'),
]
