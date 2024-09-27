from django.shortcuts import render

from .models import WorkExperience


def experience_home(request):
    work_experiences = WorkExperience.objects.all()  # Get all job experiences from the database
    return render(request, 'experience/home.html', {'work_experiences': work_experiences})

#def introduction_home(request):
 #   return render(request, 'experience/introduction.html')
