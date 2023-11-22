from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
STATUS_CHOICES = (
    ('To-Do', 'To-Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),)
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To-Do')
    
    def __str__(self):
        return f"title {self.title} id {self.id}"    
