from django.db import models as m
from tinymce.models import HTMLField

from uuid import uuid4

class Subject(m.Model):

    uid = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")

    title = m.CharField(max_length=200)
    slug = m.SlugField(unique=True)

    image = m.ImageField(upload_to='subjects/', blank=True, null=True)
    
    created_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class Topic(m.Model):
    
    uid = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")

    subject = m.ForeignKey(Subject, on_delete=m.CASCADE, related_name='topics')
    
    title = m.CharField(max_length=200)
    slug = m.SlugField(unique=True)
    
    created_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.subject.title} - {self.title}"


class Lesson(m.Model):

    uid = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")

    subject = m.ForeignKey(Subject, on_delete=m.CASCADE, related_name='lesson_subject')
    topic = m.ForeignKey(Topic, on_delete=m.CASCADE, related_name='lesson_topic')
    
    title = m.CharField(max_length=200)
    slug = m.SlugField(unique=True)
    
    content = HTMLField()  # TinyMCE for rich-text lesson content
    
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.topic.subject.title} - {self.topic.title} - {self.title}"


class Task(m.Model):

    uid = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")

    subject = m.ForeignKey(Subject, on_delete=m.CASCADE, related_name='tasks')
    lesson = m.ForeignKey(Lesson, on_delete=m.CASCADE, related_name='tasks')
    
    question = HTMLField()  # TinyMCE for task question

    correct_answer = m.CharField(max_length=255)
    answer2 = m.CharField(max_length=255)
    answer3 = m.CharField(max_length=255)
    answer4 = m.CharField(max_length=255)
    
    explanation = HTMLField()  # TinyMCE for task question

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return f"Task for {self.lesson.title}"


class AnswerOption(m.Model):

    uid = m.UUIDField(primary_key = True, default = uuid4, editable = False, verbose_name = "ID")

    task = m.ForeignKey(Task, on_delete=m.CASCADE, related_name='options')
    
    text = m.CharField(max_length=255)

    def __str__(self):

        return self.text
