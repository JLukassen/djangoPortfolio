# Create your views here.
from django.shortcuts import render
from .models import SideProject

def project_list(request):
    projects = SideProject.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})