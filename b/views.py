from django.shortcuts import render, get_object_or_404
from .models import Subject, Topic, Lesson

def landing(request):
    subjects = Subject.objects.all()
    return render(request, 'landing.html', {'subjects': subjects})

def subject(request, subject_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    topics = subject.topics.all()
    return render(request, 'subject.html', {'subject': subject, 'topics': topics})

def topic(request, subject_slug, topic_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    topic = get_object_or_404(Topic, slug=topic_slug, subject=subject)
    lessons = topic.lessons.all()
    return render(request, 'topic.html', {'subject': subject, 'topic': topic, 'lessons': lessons})

def lesson(request, subject_slug, topic_slug, lesson_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    topic = get_object_or_404(Topic, slug=topic_slug, subject=subject)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, topic=topic)
    return render(request, 'lesson.html', {'subject': subject, 'topic': topic, 'lesson': lesson})
