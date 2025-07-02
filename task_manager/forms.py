from django import forms

from .models import Goal, Task, TaskNote


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            'title',
            'content',
            'is_done',
        ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'content',
            'deadline',
            'status',
            'goal'
        ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = TaskNote
        fields = [
            'title',
            'text',
            'task',
        ]
