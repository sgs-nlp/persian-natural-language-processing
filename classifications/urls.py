from django.urls import path, include
from .views import *

app_name = 'classification'
urlpatterns = [
    path('', index, name='index'),
]
