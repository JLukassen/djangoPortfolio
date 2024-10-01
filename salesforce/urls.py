from django.urls import path
from . import views

urlpatterns = [
    path('', views.trailhead_profile, name='trailhead_profile'),
]
