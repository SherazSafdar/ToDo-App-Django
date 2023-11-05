from django.contrib import admin
from .models import TaskCategory, Task

admin.site.register(Task)
admin.site.register(TaskCategory)