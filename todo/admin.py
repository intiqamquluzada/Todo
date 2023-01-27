from django.contrib import admin

from .models import *


class TodoAdmin(admin.ModelAdmin):
    class Meta:
        model = Todo

    list_display = ('task_name', 'deadline', 'slug')


admin.site.register(Todo, TodoAdmin)
