from django.urls import path

from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('subjects/<slug:subject_slug>/', subject, name='subject'),
    path('subjects/<slug:subject_slug>/fields/<slug:field_slug>/', field, name='field'),
    path('subjects/<slug:subject_slug>/fields/<slug:field_slug>/topics/<slug:topic_slug>/', topic, name='topic'),
    path('subjects/<slug:subject_slug>/fields/<slug:field_slug>/topics/<slug:topic_slug>/lessons/<slug:lesson_slug>/', lesson, name='lesson'),
    path('ajax_search/', ajax_search, name='ajax_search'),
]
