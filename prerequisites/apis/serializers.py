from prerequisites.models import Corpus, Document, Word
from rest_framework import routers, serializers, viewsets


class CorpusListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corpus
        fields = ['id', 'name', ]


class CorpusCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corpus
        fields = ['id', 'file_path', ]


class WordRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'string', 'hash_code']


class DocumentRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    title = WordRetrieveSerializer(read_only=True, many=True)
    content = WordRetrieveSerializer(read_only=True, many=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'hash_code', 'is_completed', ]


class CorpusRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corpus
        fields = ['id', 'name', 'json_file_path']
