from uuid import uuid4
from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpRequest, HttpResponse

from .models import Goal, Task
from .forms import GoalForm, TaskForm


def goals_and_tasks(request):
    goals = Goal.objects.all()
    if request.method == 'POST':
        ordering = request.POST['tasks_order']
        tasks = Task.objects.all().order_by(ordering)
    else:
        tasks = Task.objects.all().order_by('created_at')
    data = {
        'goals': goals,
        'tasks': tasks
    }
    return render(request, 'goals_and_tasks.html', data)


def create_task(request):
    if request.method == 'POST':
        return HttpResponse('Post method')
    else:
        form = TaskForm()
    return render(request, 'create_new_task.html', {'form': form})


class AllTaskView(ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 20
    template_name = ''


class DetailTaskView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'single_task.html'

    def get(self, request: HttpRequest, task_id: uuid4, *args: Any, **kwargs: Any) -> HttpResponse:
        task = Task.objects.get(task_id=task_id)
        return render(request, self.template_name, {'task': task})


class AllGoalsView(ListView):
    model = Goal
    context_object_name = 'goals'
    paginate_by = 10
    template_name = ''


class DetailGoalView(DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = ''
