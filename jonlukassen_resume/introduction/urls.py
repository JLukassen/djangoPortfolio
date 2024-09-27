from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduction_home, name='introduction_home'),
]
