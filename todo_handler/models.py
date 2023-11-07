from django.db import models
from django.contrib.auth.models import User


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Priority(models.TextChoices):
    LOW = 'Low', 'Low Priority'
    MEDIUM = 'Medium', 'Medium Priority'
    HIGH = 'High', 'High Priority'

class Status(models.TextChoices):
    TODO = 'To-Do', 'To-Do'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)

    def __str__(self):
        return self.title
