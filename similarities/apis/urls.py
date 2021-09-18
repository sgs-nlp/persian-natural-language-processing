from django.urls import path, include
from .views import *

app_name = 'similarity_api'
urlpatterns = [
    path('', index, name='index'),
]
