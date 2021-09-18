from django.urls import path, include
from .views import *

app_name = 'plp_index'
urlpatterns = [
    path('', index, name='index'),
]
