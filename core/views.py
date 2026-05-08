from django.shortcuts import render
from .models import Project, Lead

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contact.html')

def explore_projects(request):
    return render(request, 'projects/explore_projects.html')



def project_detail(request):
    return render(request, 'projects/project_detail.html')