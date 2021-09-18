from django.urls import path, include
from .views import *

app_name = 'prerequisite_api'
urlpatterns = [
    path('', index, name='index'),
]
