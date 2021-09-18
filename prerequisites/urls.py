 
from django.urls import path, include
from .views import *

app_name = 'prerequistie'
urlpatterns = [
    path('', index, name='index'),
]
