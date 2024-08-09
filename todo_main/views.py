from django.shortcuts import render
from TODO.models import Task

def home(request):
    task = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True)
    context={
        'task' : task,
        'completed_tasks':completed_task
    }
    return render(request,'home.html',context)