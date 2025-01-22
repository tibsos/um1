from django.shortcuts import render, get_object_or_404
from .models import *

def landing(request):
    subjects = Subject.objects.all()
    return render(request, 'landing.html', {'subjects': subjects})

def subject(request, subject_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    fields = Field.objects.filter(subject=subject)
    return render(request, 'subject.html', {'subject': subject, 'fields': fields})

def field(request, subject_slug, field_slug):
    
    subject = get_object_or_404(Subject, slug=subject_slug)
    field = get_object_or_404(Field, slug=field_slug, subject=subject)
    topics = Topic.objects.filter(field=field)
    
    c = {

        'subject': subject, 
        'field': field, 
        'topics': topics, 

    }
    
    return render(request, 'field.html', c)

def topic(request, subject_slug, field_slug, topic_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    field = get_object_or_404(Field, slug=field_slug, subject=subject)
    topic = get_object_or_404(Topic, slug=topic_slug, subject=subject)
    lessons = Lesson.objects.filter(topic=topic)
 
    c = {

        'subject': subject, 
        'field': field, 
        'topic': topic, 
        'lessons': lessons

    }

    return render(request, 'topic.html', c)

def lesson(request, subject_slug, field_slug, topic_slug, lesson_slug):
    
    subject = get_object_or_404(Subject, slug=subject_slug)
    field = get_object_or_404(Field, slug=field_slug)
    topic = get_object_or_404(Topic, slug=topic_slug, subject=subject)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, topic=topic)
    
    return render(request, 'lesson.html', {'subject': subject, 'field': field, 'topic': topic, 'lesson': lesson})
