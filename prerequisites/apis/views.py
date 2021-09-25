from rest_framework import generics

from .serializers import *
from prerequisites.models import Corpus

from nvd.paginators import MediumResultsSetPagination


class CorpusGenericsListAPIView(generics.ListAPIView):
    queryset = Corpus.objects.all()
    serializer_class = CorpusListSerializer


class CorpusGenericsCreateAPIView(generics.CreateAPIView):
    queryset = Corpus.objects.all()
    serializer_class = CorpusCreateSerializer


class CorpusGenericsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Corpus.objects.all()
    serializer_class = CorpusRetrieveSerializer
    lookup_field = 'id'

    def get_context_data(self, **kwargs):
        kwargs['documents'] = self.get_object().documents.all()
        return super(CorpusGenericsRetrieveAPIView, self).get_context_data(**kwargs)
