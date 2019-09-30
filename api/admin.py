from django.contrib import admin
from api.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'active']


admin.site.register(Task, TaskAdmin)

