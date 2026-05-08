from django.shortcuts import render, redirect
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

    return render(request, 'home.html', context)

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def explore_projects(request):
    return render(request, 'projects/explore_projects.html')



def project_detail(request):
    return render(request, 'projects/project_detail.html')