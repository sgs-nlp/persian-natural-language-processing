from django.urls import path, include
from .views import *

app_name = 'stopwords_list_api'
urlpatterns = [
    path('', index, name='index'),
]
