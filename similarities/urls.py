 
from django.urls import path, include
from .views import *

app_name = 'similarity'
urlpatterns = [
    path('', index, name='index'),
]
