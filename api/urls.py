from django.urls import path
from . import views

urlpatterns = [
    path('createtask/', views.create_task, name='task-list'),
    path('retrievetask/<int:task_id>/', views.retrieve_task, name='retrieve-task'),
]