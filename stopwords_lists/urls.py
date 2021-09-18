from django.urls import path, include
from .views import *

app_name = 'stopwords_list'
urlpatterns = [
    path('', index, name='index'),
]
