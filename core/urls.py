from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
]