from django.urls import path

from .views import goals_and_tasks, create_task
from .views import AllTaskView, DetailTaskView
from .views import AllGoalsView, DetailGoalView


urlpatterns = [
    path('', goals_and_tasks, name='manager-home'),

    path('task-manager/tasks/', AllTaskView.as_view(), name='tasks-page'),
    path('task-manager/tasks/<uuid:task_id>/', DetailTaskView.as_view(), name='single-task'),
    path('tasks/create_new/', create_task, name='new-task'),

    path('goals/', AllGoalsView.as_view(), name='goals-page'),
    path('goals/<uuid:goal_id>/', DetailGoalView.as_view(), name='single-goal'),
]
