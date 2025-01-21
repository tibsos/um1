from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('pt.urls')),
    path('', include('chem.urls')),
    path('', include('b.urls')),

]
