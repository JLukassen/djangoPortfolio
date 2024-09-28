from django.urls import path
from . import views

urlpatterns = [
    path('salesforce/', views.trailhead_profile, name='trailhead_profile'),
]
