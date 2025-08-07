from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.

def task_list(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('task_list')
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
    

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})
