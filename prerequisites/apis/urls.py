from django.urls import path, include

from prerequisites.models import Corpus
from .views import *

app_name = 'prerequisite_api'
urlpatterns = [

    path('corpus', CorpusGenericsListAPIView.as_view(), name='corpus_list'),
    path('corpus/add', CorpusGenericsCreateAPIView.as_view(), name='add_corpus'),
    path('corpus/<int:id>', CorpusGenericsRetrieveAPIView.as_view(), name='details_corpus'),

]