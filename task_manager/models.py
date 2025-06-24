import uuid
from django.db import models


class Goal(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Goal Title'
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name='Goal description'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    goal_id = models.UUIDField(
        unique=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'{self.title} was created at: {self.created_at}'

    class Meta:
        ordering = ['title', '-created_at']
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'


class Task(models.Model):
    class TaskStatus(models.IntegerChoices):
        NOT_DONE = 0, 'Not Done'
        IN_PROCESS = 1, 'In Process'
        DONE = 2, 'Done'
        WASTE = 3, 'Waste'

    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Task Title'
        )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name='Task description'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )
    status = models.SmallIntegerField(
        choices=TaskStatus.choices,
        default=TaskStatus.NOT_DONE,
        verbose_name='Task status'
    )
    task_id = models.UUIDField(
        unique=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
        )
    goal = models.ForeignKey(
        Goal,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'{self.title}: {self.status}'

    class Meta:
        ordering = ['title', '-created_at',]
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class TaskNote(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Note title',

    )
    text = models.TextField(
        verbose_name='Note body',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='notes'
        )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'Note({self.title}) for Task({self.task.title})'

    class Meta:
        verbose_name = 'Task Note'
        verbose_name_plural = 'Task Notes'
        ordering = ['title', '-created_at']
