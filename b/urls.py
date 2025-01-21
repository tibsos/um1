from django.urls import path

from .views import *

urlpatterns = [

    path('', landing, name = 'landing'),
    path('<slug:subject_slug>', subject, name = 'subject'),
    path('<slug:subject_slug>/<slug:topic_slug>', topic, name = 'topic'),
    path('<slug:subject_slug>/<slug:topic_slug>/<slug:lesson_slug>', lesson, name = 'lesson'),

]