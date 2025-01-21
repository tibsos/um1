from django.contrib import admin
from .models import Subject, Topic, Lesson, Task

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["subject"]
    search_fields = ["title"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["topic"]
    search_fields = ["title", "content"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'correct_answer']
    list_filter = ['lesson']
    search_fields = ['question']
