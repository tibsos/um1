from django.urls import path

from .views import *

urlpatterns = [

    path('periodic-table', landing, name = 'landing'),

]