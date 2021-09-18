 
from django.urls import path, include
from .views import *

app_name = 'template_view'
urlpatterns = [
    path('', index, name='index'),
]
