from django.urls import path
from . import views
from .views import CreateTaskView, TaskView

urlpatterns = [
    path('v1/task/', views.create_task, name='task-list'),
    path('v1/task/<int:task_id>/', views.retrieve_task, name='retrieve-task'),
    path('v2/task/', CreateTaskView.as_view(), name='create-task'),
    path('v2/task/<int:task_id>/', TaskView.as_view(), name='tasks')
]