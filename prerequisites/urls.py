 
from django.urls import path, include
from .views import *

app_name = 'prerequistie'
urlpatterns = [
    # path('', index, name='index'),
    # path('add-corpus', add_corpus, name='add_corpus'),
    path('', add_corpus, name='add_corpus'),
]
