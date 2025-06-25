from django.contrib import admin

from .models import Goal, Task, TaskNote


class TaskInLine(admin.StackedInline):
    model = Task
    extra = 1


class NoteInLine(admin.StackedInline):
    model = TaskNote
    extra = 1


class GoalAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'content',
        'is_done',
    )
    list_display = (
        'title',
        'created_at',
        'is_done',
    )
    list_filter = (
        'is_done',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'title',
    )
    list_per_page = 20

    inlines = [
        TaskInLine,
    ]


class TaskAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'content',
        'deadline',
        'status',
        'goal',
        )
    list_display = (
        'title',
        'status',
    )
    list_filter = (
        'status',
        'created_at',
        'updated_at',
        'deadline'
    )
    search_fields = (
        'title',
        'status',
    )
    list_per_page = 20
    inlines = [
        NoteInLine,
    ]


class NoteAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'text',
        'task',
        )
    list_display = (
        'title',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
    )
    list_per_page = 20


admin.site.register(Goal, GoalAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskNote, NoteAdmin)
