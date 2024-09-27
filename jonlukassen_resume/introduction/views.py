from django.shortcuts import render

def introduction_home(request):
    return render(request, 'introduction/introduction.html')  # Make sure this matches your template path
