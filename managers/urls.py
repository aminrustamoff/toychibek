from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.management_login, name='login'),
    path('logout/', views.management_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('projects/', views.projects_list, name='projects'),
    path('projects/add/', views.project_add, name='project_add'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    path('messages/', views.messages_list, name='messages'),

    path('comments/', views.comments_list, name='comments'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
