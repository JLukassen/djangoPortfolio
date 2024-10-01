from django.urls import path
from . import views
from .views import download_resume 

urlpatterns = [
    path('', views.resume_contact, name='resume_contact'),
    path('download_resume/', download_resume, name='download_resume'),
]