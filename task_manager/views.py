from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Goal, Task


def goals_and_tasks(request):
    goals = Goal.objects.all()
    tasks = Task.objects.all()
    data = {
        'goals': goals,
        'tasks': tasks
    }
    return render(request, 'goals_and_tasks.html', data)


class AllTaskView(ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 20
    template_name = ''


class DetailTaskView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = ''


class AllGoalsView(ListView):
    model = Goal
    context_object_name = 'goals'
    paginate_by = 10
    template_name = ''


class DetailGoalView(DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = ''
