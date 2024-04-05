from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'priority', 'status', 'assigned_to', 'created_by')
    list_filter = ('status', 'priority', 'due_date', 'created_by')
    search_fields = ('title', 'description')
