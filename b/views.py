from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse

def landing(request):

    subjects = Subject.objects.all()

    return render(request, 'landing.html', {'subjects': subjects})

def subject(request, subject_slug):

    subject = get_object_or_404(Subject, slug=subject_slug)
    fields = Field.objects.filter(subject=subject)

    c = {

        'subject': subject,
        'fields': fields,

    }

    return render(request, 'subject.html', c)

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

def ajax_search(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse({'results': []})  # Пустой ответ, если нет запроса

    # Фильтрация данных
    subjects = Subject.objects.filter(title__icontains=query).values('title', 'slug')
    fields = Field.objects.filter(title__icontains=query).values('title', 'slug', 'subject__slug')
    topics = Topic.objects.filter(title__icontains=query).values('title', 'slug', 'field__slug', 'field__subject__slug')
    lessons = Lesson.objects.filter(title__icontains=query).values(
        'title', 'slug', 'topic__slug', 'topic__field__slug', 'topic__field__subject__slug'
    )

    # Формирование данных для фронтенда
    results = {
        'subjects': [{'title': item['title'], 'url': f'/{item["slug"]}/'} for item in subjects],
        'fields': [{'title': item['title'], 'url': f'/{item["subject__slug"]}/{item["slug"]}/'} for item in fields],
        'topics': [{'title': item['title'], 'url': f'/{item["field__subject__slug"]}/{item["field__slug"]}/{item["slug"]}/'} for item in topics],
        'lessons': [{'title': item['title'], 'url': f'/{item["topic__field__subject__slug"]}/{item["topic__field__slug"]}/{item["topic__slug"]}/{item["slug"]}/'} for item in lessons],
    }
    return JsonResponse({'results': results})
