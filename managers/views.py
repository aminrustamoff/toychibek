from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.contrib import messages as django_messages
from django.http import JsonResponse
from core.models import Comments, Contact, Project, Lead, AdminPanel
from .forms import ProjectForm


def management_login(request):
    if request.user.is_authenticated:
        return redirect('management:dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect('management:dashboard')
        else:
            error = "Login yoki parol noto'g'ri."

    return render(request, 'management/login.html', {'error': error})


def management_logout(request):
    logout(request)
    return redirect('management:login')


@login_required(login_url='/management/')
def dashboard(request):
    total_projects = Project.objects.count()
    total_leads = Lead.objects.count()
    total_budget = AdminPanel.objects.aggregate(total=Sum('budget'))['total'] or 0
    total_available = Project.objects.aggregate(total=Sum('available_numbers'))['total'] or 0
    unread_messages = Contact.objects.filter(is_read=False).count()
    recent_leads = Lead.objects.select_related('project').order_by('-created_at')[:5]
    projects_by_status = {
        'active': Project.objects.filter(status='active').count(),
        'sold_out': Project.objects.filter(status='sold_out').count(),
        'upcoming': Project.objects.filter(status='upcoming').count(),
    }

    context = {
        'total_projects': total_projects,
        'total_leads': total_leads,
        'total_budget': total_budget,
        'total_available': total_available,
        'unread_messages': unread_messages,
        'recent_leads': recent_leads,
        'projects_by_status': projects_by_status,
    }
    return render(request, 'management/dashboard.html', context)


@login_required(login_url='/management/')
def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'management/projects.html', {'projects': projects})


@login_required(login_url='/management/')
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            django_messages.success(request, "Loyiha muvaffaqiyatli qo'shildi.")
            return redirect('management:projects')
    else:
        form = ProjectForm()
    return render(request, 'management/project_form.html', {
        'form': form,
        'title': "Yangi loyiha qo'shish",
        'action': 'add'
    })


@login_required(login_url='/management/')
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            django_messages.success(request, "Loyiha muvaffaqiyatli yangilandi.")
            return redirect('management:projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'management/project_form.html', {
        'form': form,
        'title': "Loyihani tahrirlash",
        'action': 'edit',
        'project': project
    })


@login_required(login_url='/management/')
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        django_messages.success(request, "Loyiha o'chirildi.")
    return redirect('management:projects')


@login_required(login_url='/management/')
def messages_list(request):
    contacts = Contact.objects.all()
    # Mark as read when viewed
    Contact.objects.filter(is_read=False).update(is_read=True)
    return render(request, 'management/messages.html', {'contacts': contacts})


@login_required(login_url='/management/')
def comments_list(request):
    comments = Comments.objects.all()
    return render(request, 'management/comments.html', {'comments': comments})


@login_required(login_url='/management/')
def comment_delete(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    if request.method == 'POST':
        comment.delete()
        django_messages.success(request, "Izoh o'chirildi.")
    return redirect('management:comments')
