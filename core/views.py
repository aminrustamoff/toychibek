from django.shortcuts import render
from .models import Project, Lead

# Create your views here.

def home(request):
    return render(request, 'home.html')

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/detail.html', {'project': project})