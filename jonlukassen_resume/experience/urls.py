from django.urls import path
from . import views

urlpatterns = [
    path('', views.experience_home, name='experience_home'),
]
