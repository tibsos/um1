from django.urls import path

from .views import *

urlpatterns = [

    path('chem-instruments', base, name = 'landing'),

]