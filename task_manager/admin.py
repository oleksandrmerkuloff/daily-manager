from django.contrib import admin

from .models import Goal, Task, TaskNote


class GoalAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
        'is_done',
    ]
    list_display = [
        'title',
        'created_at',
        'is_done',
    ]
    list_filter = [
        'is_done',
        'created_at',
        'updated_at'
    ]
    search_fields = [
        'title',
    ]
    list_per_page = 20


admin.site.register(Goal, GoalAdmin)
admin.site.register(Task)
admin.site.register(TaskNote)
