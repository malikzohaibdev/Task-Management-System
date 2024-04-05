import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from tasks.tasks import send_task_notification_email
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User

@login_required
def task_list(request):
    # Filtering tasks based on the logged-in user (either created by or assigned to them)
    tasks = Task.objects.filter(created_by=request.user) | Task.objects.filter(assigned_to=request.user)
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    try:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.created_by = request.user
                task.save()
                return redirect('task-list')
        else:
            form = TaskForm()
            # Set the initial value for `assigned_to` to the current user
            form.fields['assigned_to'].queryset = User.objects.exclude(id=request.user.id)
        return render(request, 'tasks/task_form.html', {'form': form})
    except Exception as e:
        msg = "Error [{0}] at line [{1}]".format(str(e), sys.exc_info()[2].tb_lineno)
        print(msg)

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
        form.fields['assigned_to'].queryset = User.objects.exclude(id=request.user.id)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
