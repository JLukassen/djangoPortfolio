from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.resume_contact, name='resume_contact'),
]