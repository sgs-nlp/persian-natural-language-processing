import os

from django.db import models

from nvd.hasher import list_hash, string_hash

from conf.settings import BASE_DICT

from prerequisites.models import Word, Corpus


class Stopword(models.Model):
    word = models.ForeignKey(
        to=Word,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    corpus = models.ForeignKey(
        to=Corpus,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    hash_code = models.CharField(
        max_length=512,
        unique=True,
        null=False,
        blank=False
    )


def stoword2db(word_id: int, corpus_id: int) -> int:
    stopword_hash = list_hash([word_id, corpus_id])
    stopword = BASE_DICT.get_item(stopword_hash)
    if stopword is None:
        stopword = Stopword()
        stopword.word_id = word_id
        stopword.corpus_id = corpus_id
        stopword.hash_code = stopword_hash
        stopword.save()
        BASE_DICT.set_item(stopword_hash, stopword)
    return stopword
