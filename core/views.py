from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, ContactForm
from .models import Comments, Contact, Project, Lead

# Create your views here.

def home(request):
    comments = Comments.objects.all().order_by('-created_at')[:6]

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()

    context = {
        'comments': comments,
        'form': form
    }

    return render(request, 'core/home.html', context)

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def explore_projects(request):

    projects = Project.objects.all()
    return render(request, 'core/projects/explore_projects.html', {'projects': projects})



def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'core/projects/project_detail.html', {'project': project})