 
from django.urls import path, include
from .views import *

app_name = 'keywords_extraction'
urlpatterns = [
    path('', index, name='index'),
]
