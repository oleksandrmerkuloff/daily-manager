from django.urls import path

from .views import goals_and_tasks
from .views import AllTaskView, DetailTaskView
from .views import AllGoalsView, DetailGoalView


urlpatterns = [
    path('', goals_and_tasks, name='task_home'),

    path('tasks/', AllTaskView.as_view(), name='tasks-page'),
    path('tasks/<uuid:task_id>/', DetailTaskView.as_view(), name='single-task'),

    path('goals/', AllGoalsView.as_view(), name='goals-page'),
    path('goals/<uuid:goal_id>/', DetailGoalView.as_view(), name='single-goal'),
]
