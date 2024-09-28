from django.urls import path
from . import views

urlpatterns = [
    path('experience', views.experience_home, name='experience_home'),  # Base URL for /experience/
]
