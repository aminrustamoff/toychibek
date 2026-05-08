from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('explore-projects/', views.explore_projects, name='explore_projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
]